import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('/homepage.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('/login.html')
        self.response.write(login_template.render())

class SignUpPage(webapp2.RequestHandler):
    def get(self):
        signup_template = the_jinja_env.get_template('/signup.html')
        self.response.write(signup_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', LoginPage),
    ('/signup', SignUpPage) #this maps the root url to the Main Page Handler
], debug=True)
