from google.appengine.ext import db
class Signup(db.Model):
  email = db.EmailProperty()
  language = db.StringProperty()
  