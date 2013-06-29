import os
import jinja2
import webapp2
from google.appengine.api import users

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        login_url = users.create_login_url('/secret')
        logout_url = users.create_logout_url('/')
        
        template = template_env.get_template('templates/index.html')
        context = {
            'user' : user,
            'login_url' : login_url,
            'logout_url' : logout_url
        }
        self.response.out.write(template.render(context))    
        
class SecretPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/secret.html')
        logout_url = users.create_logout_url('/')
        context = {'logout_url' : logout_url}
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/secret', SecretPage)],
                                      debug=True)