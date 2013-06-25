import datetime
import jinja2
import webapp2
import os
import models

from google.appengine.api import users

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        nickname = ''
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.path)
        logout_url = users.create_logout_url(self.request.path)
        
        userprefs = models.get_userprefs()
        if userprefs:
            nickname = userprefs.nickname
        
        template = template_env.get_template('home.html')
        context = {
            'nickname'     : nickname,
            'user'         : user,
            'login_url'    : login_url,
            'logout_url'   : logout_url,
            'userprefs'    : userprefs,
            'texto_dummy'  : os.environ.get("TEXTO_DUMMY")
        }        
        self.response.out.write(template.render(context))
    
application = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)