import webapp2
import jinja2
import os
import time
import logging
import pytz
from pytz import timezone
# from model import UserDataStore
from google.appengine.ext import ndb
from model import MessageDataStore
from model import ProfileStore
from model import CssiUser
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      email_address = user.nickname()
      cssi_user = CssiUser.query().filter(CssiUser.email == email_address).get()
      self.response.write(signout_link_html)
      # If the user is registered...
      print('does this worl')
      self.redirect('/profile')
    else:
      # If the user isn't logged in...
      login_url = users.create_login_url('/profile')
      login_html_element = '<a href="%s">Sign in</a>' % login_url
      # Prompt the user to sign in.
      self.response.write('Please log in.<br>' + login_html_element)

  def post(self):
    # Code to handle a first-time registration from the form:
    user = users.get_current_user()
    cssi_user = CssiUser(
        username=self.request.get('username'),
        psw=self.request.get('psw'),
        email=user.nickname())
    cssi_user.put()
    self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
        cssi_user.username)



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
    #     error = self.request.get('error')
    #     new_dic = {
    #         'errormessage': error
    #     }
        self.response.write(login_template.render())
    #
    # def post(self):
    #     username_query = UserDataStore.query()
    #     users = username_query.fetch()
    #     print(users)
    #     for x in users:
    #         if x.psw == self.request.get('psw') and x.username == self.request.get('uname'):
    #             self.redirect('/profile')
    #             return
    #     self.redirect('/login?error=not-found')
    #     return

class SignUpPage(webapp2.RequestHandler):
    def get(self):
        signup_template = the_jinja_env.get_template('/signup.html')
        self.response.write(signup_template.render())

    def post(self):
        email = self.request.get('email')
        username = self.request.get('username')
        password = self.request.get('psw')
        passwordRepeat = self.request.get('psw-repeat')

        # userlogin = UserDataStore(username=username, psw=password)
        # userlogin.put()
        self.redirect('/login')

class ProfilePage(webapp2.RequestHandler):
        def get(self):
            cssi_user = ProfileStore.query().filter(ProfileStore.email == users.get_current_user().nickname()).get()
            profiledic = {
                'profileInfo': cssi_user
            }
            profile_template = the_jinja_env.get_template('/profile.html')
            self.response.write(profile_template.render(profiledic))
            user = users.get_current_user()
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
            accounting = self.request.get('accounting') == "on";
            business = self.request.get('business') == "on";
            construction = self.request.get('construction') == "on";
            finance = self.request.get('finance') == "on";
            health_care = self.request.get('health_care') == "on";
            media = self.request.get('media') == "on";
            manufacturing = self.request.get('manufacturing') == "on";
            restaraunt = self.request.get('restaraunt') == "on";
            retail = self.request.get('retail') == "on";
            technology = self.request.get('technology') == "on";
            other = self.request.get('other') == "on";
            twofivek = self.request.get('twofivek') == "on";
            fiveok = self.request.get('fiveok') == "on";
            sevenfivek = self.request.get('sevenfivek') == "on";
            onehunnidk = self.request.get('onehunnidk') == "on";
            onefiftyk = self.request.get('onefiftyk') == "on";
            bigballerbrand = self.request.get('bigballerbrand') == "on";

            city = self.request.get('city')
            state = self.request.get('state')
            zip_code = self.request.get('zip_code')
            email = users.get_current_user().nickname()
            print("Email " + email)
            user_query = ProfileStore.query().filter(ProfileStore.email == email)
            user_list = user_query.fetch()

            print("user_list =" + str(user_list))

            profileInfo = None
            if len(user_list) == 1 :
                user_current = user_list[0]
                user_current.first_name=first_name
                user_current.last_name=last_name
                user_current.username=username
                user_current.password=password
                user_current.age=age
                user_current.gender=gender
                user_current.race_indian=race_indian
                user_current.race_asian=race_asian
                user_current.race_african=race_african
                user_current.race_hawaiian=race_hawaiian
                user_current.race_white=race_white
                user_current.ethnicity_indian=ethnicity_indian
                user_current.ethnicity_asian=ethnicity_asian
                user_current.ethnicity_african=ethnicity_african
                user_current.ethnicity_hawaiian=ethnicity_hawaiian
                user_current.ethnicity_white=ethnicity_white
                user_current.sex_orient=sex_orient
                user_current.city=city
                user_current.state=state
                user_current.zip_code=zip_code
                user_current.email=email
                user_current.accounting=accounting
                user_current.business=business
                user_current.construction=construction
                user_current.finance=finance
                user_current.health_care=health_care
                user_current.media=media
                user_current.manufacturing=manufacturing
                user_current.restaraunt=restaraunt
                user_current.retail=retail
                user_current.technology=technology
                user_current.other=other
                user_current.twofivek=twofivek
                user_current.fiveok=fiveok
                user_current.sevenfivek=sevenfivek
                user_current.onehunnidk=onehunnidk
                user_current.onefiftyk=onefiftyk
                user_current.bigballerbrand=bigballerbrand
                user_current.put()
                profileInfo = user_current

            else:
                profileInfo = ProfileStore(first_name=first_name, last_name=last_name,
                                            username=username, password=password, age=age, gender=gender, race_indian=race_indian, race_asian=race_asian, race_african=race_african, race_hawaiian=race_hawaiian, race_white=race_white, ethnicity_indian=ethnicity_indian, ethnicity_asian=ethnicity_asian, ethnicity_african=ethnicity_african, ethnicity_hawaiian=ethnicity_hawaiian, ethnicity_white=ethnicity_white, sex_orient=sex_orient, city=city, state=state, zip_code=zip_code, email=email,
                                            accounting=accounting, business=business, construction=construction, finance=finance,
                                            health_care=health_care, media=media, manufacturing=manufacturing, restaraunt=restaraunt,
                                            retail=retail, technology=technology, other=other, twofivek=twofivek, fiveok=fiveok,
                                            sevenfivek=sevenfivek, onehunnidk=onehunnidk, onefiftyk=onefiftyk,
                                            bigballerbrand=bigballerbrand)

                profileInfo.put()
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
        user = users.get_current_user()
        nickname = user.nickname()
        status = self.request.get("CurrentStatus")

        messagestore = MessageDataStore(CurrentStatus=status, username=nickname)
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
        friend_query = ProfileStore.query()
        friends = friend_query.fetch()
        suggestion_template = the_jinja_env.get_template('/suggestions.html')
        friends_dict = {
            "friends": friends
        }
        self.response.write(suggestion_template.render(friends_dict))

class SignoutPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # If the user is logged in...
        if user:
          signout_link_html = '<a href="%s">sign out</a>' % (
              users.create_logout_url('/'))
          self.response.write(signout_link_html)
          # If the user is registered...
          self.redirect(users.create_logout_url('/'))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', MainHandler),
    ('/signup', SignUpPage),
    ('/profile', ProfilePage),
    ('/friends', FriendsPage),
    ('/messages', MessagesPage),
    ('/aboutus', AboutPage),
    ('/suggestions', SuggestionsPage),
    ('/signout', SignoutPage),
], debug=True)
