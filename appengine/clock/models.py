from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.ext import db
import logging

class UserPrefs(db.Model):
    nickname = db.StringProperty()
    user = db.UserProperty(auto_current_user_add=True)
    
    def cache_set(self):
        logging.info('cache set')        
        memcache.set('UserPrefs:' + self.key().name(), self)
        
    def put(self): 
        super(UserPrefs, self).put()
        self.cache_set()
    
def get_userprefs(user_id=None):
    if not user_id:
        user = users.get_current_user()
        if not user:
            return None
        user_id = user.user_id()
    
    userprefs = memcache.get('UserPrefs:' + user_id)
    if not userprefs:
        key = db.Key.from_path('UserPrefs', user_id)
        userprefs = db.get(key)
        if userprefs:
            userprefs.cache_set()
        else:
            userprefs = UserPrefs(key_name=user_id)
    return userprefs