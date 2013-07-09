import webapp2
import os
import jinja2
from models import Producto
from google.appengine.ext import db
from datetime import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        #si no hay registros, entonces poblar       
        if Producto.all().count() == 0:        
            self.populate()
                    
        #filtros
        radio = self.request.get('radio')
        nombre = self.request.get('nombre')
        stock_op = self.request.get('stock_op')
        stock = self.request.get('stock')
        expiracion_op = self.request.get('expiracion_op')
        expiracion = self.request.get('expiracion')
        precio_op = self.request.get('precio_op')
        precio = self.request.get('precio')
                
        query = "SELECT * FROM Producto"
        query_params = []
        if radio == "nombre" and nombre != "":
            query += " WHERE nombre = '" + nombre + "'"
        if radio == "stock" and stock_op != "" and stock != "":
            query += " WHERE stock " + stock_op + " " + stock    
        if radio == "expiracion" and expiracion_op != "" and expiracion != "":
            fecha = datetime.strptime('2012-02-10' , '%Y-%m-%d')                     
            query += " WHERE expiracion " + expiracion_op + "DATE("+expiracion[0:4]+", " + expiracion[5:7] +", " + expiracion[8:]+ ")"    
        if radio == "precio" and precio_op != "" and precio != "":
            query += " WHERE precio " + precio_op + " " + precio            
                                                                    
        productos = db.GqlQuery(query)

        context = {
            "radio"         : radio,
            "productos"     : productos,
            "query"         : query,
            "nombre"        : nombre,
            "stock_op"      : stock_op,
            "stock"         : stock,
            "expiracion_op" : expiracion_op,
            "expiracion"    : expiracion,
            "precio_op"     : precio_op,     
            "precio"        : precio            
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