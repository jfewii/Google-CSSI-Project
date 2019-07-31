import webapp2
import jinja2
import os
import time
import logging
import pytz
from pytz import timezone
from model import UserDataStore
from google.appengine.ext import ndb
from model import MessageDataStore
from model import ProfileStore

def datetimefilter(value, format="%R %m-%d-%Y"):
    tz = pytz.timezone('US/Pacific') # timezone you want to convert to from UTC
    utc = pytz.timezone('UTC')
    value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
    local_dt = value.astimezone(tz)
    return local_dt.strftime(format)

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

the_jinja_env.filters["datetimefilter"]=datetimefilter

class MainPage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('/homepage.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('/login.html')
        error = self.request.get('error')
        new_dic = {
            'errormessage': error
        }
        self.response.write(login_template.render(new_dic))

    def post(self):
        username_query = UserDataStore.query()
        users = username_query.fetch()
        print(users)
        for x in users:
            if x.psw == self.request.get('psw') and x.username == self.request.get('uname'):
                self.redirect('/profile')
                return
        self.redirect('/login?error=not-found')
        return

class SignUpPage(webapp2.RequestHandler):
    def get(self):
        signup_template = the_jinja_env.get_template('/signup.html')
        self.response.write(signup_template.render())

    def post(self):
        username = self.request.get('username')
        password = self.request.get('psw')
        passwordRepeat = self.request.get('psw-repeat')

        userlogin = UserDataStore(username=username, psw=password)
        userlogin.put()
        self.redirect('/login')

class ProfilePage(webapp2.RequestHandler):
        def get(self):
            profile_template = the_jinja_env.get_template('/profile.html')
            self.response.write(profile_template.render())
                # check whether user is in database
        def post(self):
            first_name = self.request.get('first_name')
            last_name = self.request.get('last_name')
            username = self.request.get('username')
            password = self.request.get('password')
            age = self.request.get('age')
            gender = self.request.get('gender')
            race_indian = self.request.get('race_indian') == "on";
            race_asian = self.request.get('race_asian') == "on";
            race_african = self.request.get('race_african') == "on";
            race_hawaiian = self.request.get('race_hawaiian') == "on";
            race_white = self.request.get('race_white') == "on";
            ethnicity_indian = self.request.get('ethnicity_indian') == "on";
            ethnicity_asian = self.request.get('ethnicity_asian') == "on";
            ethnicity_african = self.request.get('ethnicity_african') == "on";
            ethnicity_hawaiian = self.request.get('ethnicity_hawaiian') == "on";
            ethnicity_white = self.request.get('ethnicity_white') == "on";
            sex_orient = self.request.get('sex_orient')
            city = self.request.get('city')
            state = self.request.get('state')
            zip_code = self.request.get('zip_code')

            profileInfo = ProfileStore(first_name=first_name, last_name=last_name, username=username, password=password, age=age, gender=gender, race_indian=race_indian, race_asian=race_asian, race_african=race_african, race_hawaiian=race_hawaiian, race_white=race_white, ethnicity_indian=ethnicity_indian, ethnicity_asian=ethnicity_asian, ethnicity_african=ethnicity_african, ethnicity_hawaiian=ethnicity_hawaiian, ethnicity_white=ethnicity_white, sex_orient=sex_orient, city=city, state=state, zip_code=zip_code)
            profileInfo.put()
            logging.info(profileInfo)
            profilelog = {
                'profileInfo': profileInfo
            }
            profile_template = the_jinja_env.get_template('/profile.html')
            self.response.write(profile_template.render(profilelog))

class FriendsPage(webapp2.RequestHandler):
    def get(self):
        friends_template = the_jinja_env.get_template('/friends.html')
        status_query = MessageDataStore.query().order(-MessageDataStore.StatusTime)
        messagecollection = status_query.fetch()

        the_variable_dict = {
        'statuses': messagecollection,
        }
        self.response.write(friends_template.render(the_variable_dict))

    def post(self):
        friends_template = the_jinja_env.get_template('/friends.html')
        status = self.request.get("CurrentStatus")
        timeStamp = self.request.get("StatusTime")

        messagestore = MessageDataStore(CurrentStatus=status)
        messagestore.put()
        time.sleep(0.1)

        self.redirect('/friends')

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
    ('/suggestions', SuggestionsPage),
], debug=True)
