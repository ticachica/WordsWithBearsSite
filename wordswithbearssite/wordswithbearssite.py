import cgi
import webapp2
import jinja2
import os
from models import *
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('templates/dashboard.html')
    template_values = {}
    self.response.out.write(template.render(template_values))

class Thanks(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('templates/thanks.html')
    template_values = {}
    self.response.out.write(template.render(template_values))

class Guestbook(webapp2.RequestHandler):
  def post(self):
    self.response.out.write('<html><body>You wrote:<pre>')
    self.response.out.write("email: "+self.request.get('email')+" language:"+self.request.get('language'))
    self.response.out.write('</pre></body></html>')
    new_signup = Signup()
    new_signup.email = self.request.get('email')
    new_signup.language = self.request.get('language')
    new_signup.put()
    self.redirect('/thanks')

class InterestedPeople(webapp2.RequestHandler):
  def get(self):
    signups = Signup.all()
    x = 0
    #self.response.out.write(signups.to_xml())
    for s in signups.fetch(1000):
      if s.email is not None:
        self.response.out.write("Signup number "+str(x)+" Email: "+str(s.email)+" Language: "+s.language+"<br/>")
      x+=1
app = webapp2.WSGIApplication([('/', MainPage),
                                ('/sign', Guestbook),
                                ('/thanks', Thanks),
                                ('/people', InterestedPeople)],
                              debug=True)