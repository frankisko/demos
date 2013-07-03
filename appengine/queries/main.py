import webapp2
import os
import jinja2
from models import Producto
from google.appengine.ext import db
import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        #si no hay registros, entonces poblar       
        if Producto.all().count() == 0:        
            self.populate()
                    
        #filtros
        nombre = self.request.get('nombre')
        stock = self.request.get('stock')
        expiracion = self.request.get('expiracion')
        precio = self.request.get('precio1')
                
        query = "SELECT * FROM Producto"
        query_params = []
        if nombre != "":
            query_params.append("nombre = '" + nombre + "'")
        if stock != "":
            query_params.append("stock " + stock)    
        if expiracion != "":
            query_params.append("expiracion " + expiracion)    
        if precio != "":
            query_params.append("precio " + precio)            
        
        if len(query_params) > 0:
            primero = query_params[0:1]
            query += " WHERE " +  str(primero[0]) + " AND ".join(query_params[1:])
          
        print query          
        #productos = db.GqlQuery(query)        
        context = {
         #   "productos" : productos,
            "query"     : query,
            "nombre"    : nombre,
            "stock"     : stock,
            "expiracion": expiracion,
            "precio"    : precio            
        }
        
        template = template_env.get_template('templates/index.html')        
        self.response.out.write(template.render(context))
    
    def populate(self):            
        producto = Producto(nombre="Producto 1", stock=5, expiracion = datetime.date(2013, 7, 24), precio= 32.5)
        producto.put()
        producto = Producto(nombre="Producto 2", stock=4, expiracion = datetime.date(2013, 8, 5), precio= 23.10)
        producto.put()
        producto = Producto(nombre="Producto 3", stock=10, expiracion = datetime.date(2013, 6, 9), precio= 6.75)
        producto.put()
        producto = Producto(nombre="Producto 4", stock=7, expiracion = datetime.date(2013, 9, 11), precio= 2.50)
        producto.put()
        producto = Producto(nombre="Producto 5", stock=2, expiracion = datetime.date(2013, 5, 20), precio= 16.0)
        producto.put()

application = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)