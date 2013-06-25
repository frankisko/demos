from google.appengine.ext import db

class Usuario(db.Model):
    nombre = db.StringProperty()
    apellido_paterno = db.StringProperty()
    apellido_materno = db.StringProperty()
    edad = db.IntegerProperty()    