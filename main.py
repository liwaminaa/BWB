
import webapp2, os, jinja2

from google.appengine.api import users #Google login
from google.appengine.ext import ndb #Cloud storage

#Say where you are keeping your HTML templates for Jinja2
template_directory = os.path.join(os.path.dirname(__file__), 'templates')
#Create a Jinja environment object by passing it the template location
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('BWB.html')
        self.response.out.write(template.render())

class AboutMeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutme.html')
        self.response.out.write(template.render())

class AccountMeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('account.html')
        self.response.out.write(template.render())

class CreatorsMeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('creators.html')
        self.response.out.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/aboutme', AboutMeHandler),
    ('/account', AccountMeHandler),
    ('/creators',CreatorsMeHandler)
], debug=True)
