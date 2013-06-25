from google.appengine.ext import db
import os
import webapp2
import jinja2
import logging

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class Usuario(db.Model):
	nombre = db.StringProperty()
	apellido_paterno = db.StringProperty()
	apellido_materno = db.StringProperty()
	edad = db.IntegerProperty()
	
class MainPage(webapp2.RequestHandler):
	def get(self):
		usuarios = db.Query(Usuario)
		#Usuario.all()
		
		'''
		usuarios = db.GqlQuery("""SELECT * 
								FROM Usuario
								WHERE edad > 0
								AND edad < 18
								ORDER BY edad DESC""")'''
		
		template = template_env.get_template('usuarios_index.html')
		context = {
			"usuarios" : usuarios				
	    }        
		self.response.out.write(template.render(context))
	
class AddPage(webapp2.RequestHandler):
	def get(self):
		template = template_env.get_template('usuarios_add.html')
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
		self.redirect('/crud')                

class EditPage(webapp2.RequestHandler):
	def get(self, key):
		usuario = db.get(key)
		template = template_env.get_template('usuarios_edit.html')
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
		self.redirect('/crud')
	
class DeletePage(webapp2.RequestHandler):
	def get(self, key):		
		usuario = db.get(key)
		usuario.delete()		
		self.redirect('/crud')
	
application = webapp2.WSGIApplication([('/crud', MainPage),
									   ('/crud/add', AddPage),
									   ('/crud/edit/(.*)', EditPage),
									   ('/crud/delete/(.*)', DeletePage)], 
										debug=True)