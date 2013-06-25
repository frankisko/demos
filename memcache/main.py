import webapp2
import os
import jinja2
from google.appengine.api import memcache
import logging

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
	def get(self):
		template = template_env.get_template('templates/index.html')
		context = {}
		self.response.out.write(template.render(context))
	def post(self):
		template = template_env.get_template('templates/index.html')
		context = {}					
		nombre = self.request.get('nombre')	
		cached = memcache.get(nombre)
		if not cached:
			context['info'] = "Se ha guardado tu sobrenombre"
			memcache.set(nombre, self.request.get('sobrenombre'))
		else :
			context['sobrenombre'] = cached
		self.response.out.write(template.render(context))			
	
application = webapp2.WSGIApplication([('/', MainPage),],
									debug=True)