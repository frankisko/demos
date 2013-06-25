import webapp2
import models

class CuentaPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Esta pagina solo se puede ver si estas logeado')
        
application = webapp2.WSGIApplication([('/cuenta', CuentaPage)], debug=True)

