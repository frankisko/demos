import os
import jinja2
import webapp2

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/index.html')
        context = {}
        self.response.out.write(template.render(context)) 

application = webapp2.WSGIApplication([('/custom_page', MainPage)],
                                      debug=True)