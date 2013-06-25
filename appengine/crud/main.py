import os
import webapp2
import jinja2
from google.appengine.ext import db
from models import Usuario

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):        
        usuarios = db.Query(Usuario)
        #usuarios = Usuario.all()
        
        '''
        usuarios = db.GqlQuery("""SELECT * 
                                FROM Usuario
                                WHERE edad > 0
                                AND edad < 18
                                ORDER BY edad DESC""")'''
        
        template = template_env.get_template('templates/index.html')
        context = {
            "usuarios" : usuarios                
        }        
        self.response.out.write(template.render(context))
    
class AddPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/add.html')
        context = {
        }        
        self.response.out.write(template.render(context))
    def post(self):
        usuario = Usuario(
            nombre = self.request.get("nombre"),
            apellido_paterno = self.request.get("apellido_paterno"),
            apellido_materno = self.request.get("apellido_materno"),
            edad = int(self.request.get("edad"))
        )
        usuario.put()
        self.redirect('/')                

class EditPage(webapp2.RequestHandler):
    def get(self, key):
        usuario = db.get(key)
        template = template_env.get_template('templates/edit.html')
        context = {
            "usuario" : usuario
        }        
        self.response.out.write(template.render(context))
    def post(self, key):
        usuario = db.get(key)
        usuario.nombre = self.request.get("nombre")        
        usuario.apellido_paterno = self.request.get("apellido_paterno")
        usuario.apellido_materno = self.request.get("apellido_materno")
        usuario.edad = int(self.request.get("edad"))        
        usuario.put()      
        self.redirect('/')
    
class DeletePage(webapp2.RequestHandler):
    def get(self, key):        
        usuario = db.get(key)
        usuario.delete()        
        self.redirect('/')
    
application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/add', AddPage),
                                       ('/edit/(.*)', EditPage),
                                       ('/delete/(.*)', DeletePage)], 
                                        debug=True)