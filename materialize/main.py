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

class ProfilePage(webapp2.RequestHandler):
        def get(self):
            profile_template = the_jinja_env.get_template('/profile.html')
            self.response.write(profile_template.render())

class FriendsPage(webapp2.RequestHandler):
    def get(self):
        friends_template = the_jinja_env.get_template('/friends.html')
        self.response.write(friends_template.render())

class MessagesPage(webapp2.RequestHandler):
    def get(self):
        messages_template = the_jinja_env.get_template('/messages.html')
        self.response.write(messages_template.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('/aboutus.html')
        self.response.write(about_template.render())

class SuggestionsPage(webapp2.RequestHandler):
    def get(self):
        suggestion_template = the_jinja_env.get_template('/suggestions.html')
        self.response.write(suggestion_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', LoginPage),
    ('/signup', SignUpPage),
    ('/profile', ProfilePage),
    ('/friends', FriendsPage),
    ('/messages', MessagesPage),
    ('/aboutus', AboutPage),
    ('/suggestions', SuggestionsPage)
], debug=True)
