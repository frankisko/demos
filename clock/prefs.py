import webapp2
import models

class PrefsPage(webapp2.RequestHandler):
    def post(self):
        userprefs = models.get_userprefs()
        try:
            nickname = self.request.get('nickname')
            userprefs.nickname = nickname
            userprefs.put()
        except ValueError:
            pass
        self.redirect('/')

application = webapp2.WSGIApplication([('/prefs', PrefsPage)], debug=True)

