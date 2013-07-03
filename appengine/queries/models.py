from google.appengine.ext import db

class Producto(db.Model):
    nombre = db.StringProperty()
    stock = db.IntegerProperty()
    expiracion = db.DateProperty()
    precio = db.FloatProperty()