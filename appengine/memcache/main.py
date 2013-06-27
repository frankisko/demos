import webapp2
import os
import jinja2
from google.appengine.api import memcache
import logging

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
	def get(self):
		nombre_cache = 'mi_cache'
		cached = memcache.get(nombre_cache)					
		
		if not cached:
			logging.info('No existe cache. Se procede a guardar...')				
			template = template_env.get_template('templates/index.html')
			context = {}
			html = template.render(context)
			memcache.set(nombre_cache, html, 300)
			self.response.out.write(html)			        
		else :
			logging.info('Se ha leido la informacion desde la cache')
			self.response.out.write(cached)			
	
application = webapp2.WSGIApplication([('/', MainPage),],
									debug=True)