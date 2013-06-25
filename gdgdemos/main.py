import jinja2
import webapp2
import os

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/views/site/index.html')
        context = {
        }
        self.response.out.write(template.render(context))

class MapsPage(webapp2.RequestHandler):
    def get(self, page):
        context = {
            "context_scripts" : {
                "syntax_highlighter"    : {}, 
                "google_maps"           : {"init" : True},
                "tabs"                  : {}
            }
        }
        template = template_env.get_template('templates/views/maps/' + page + '.html')
        self.response.out.write(template.render(context))
        
class FusionTablesPage(webapp2.RequestHandler):
    def get(self, page):
        context = {
            "context_scripts" : {
                "syntax_highlighter"    : {}, 
                "google_maps"           : {"init" : False},
                "tabs"                  : {}
            }
        }
        template = template_env.get_template('templates/views/fusion_tables/' + page + '.html')
        self.response.out.write(template.render(context))
        
class AppEnginePage(webapp2.RequestHandler):
    def get(self, page):
        context = {
        }
        template = template_env.get_template('templates/views/app_engine/' + page + '.html')
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/maps/(.*)', MapsPage),
                                       ('/fusion_tables/(.*)', FusionTablesPage),
                                       ('/app_engine/(.*)', AppEnginePage)], 
                                      debug=True)