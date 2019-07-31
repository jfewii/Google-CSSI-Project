# import webapp2
#
# from google.appengine.ext import ndb
#
# class CssiUser(ndb.Model):
#   first_name = ndb.StringProperty()
#   last_name = ndb.StringProperty()
#   email = ndb.StringProperty()

from google.appengine.ext import ndb
from google.appengine.api import users
import webapp2

class CssiUser(ndb.Model):
  username= ndb.StringProperty()
  psw = ndb.StringProperty()
  email = ndb.StringProperty()



# class UserDataStore(ndb.Model):
    # username = ndb.StringProperty()
    # psw = ndb.StringProperty()


class MessageDataStore(ndb.Model):
    username = ndb.StringProperty()
    CurrentStatus = ndb.StringProperty()
    StatusTime = ndb.DateTimeProperty(auto_now_add=True)


class ProfileStore(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    age = ndb.StringProperty()
    gender = ndb.StringProperty()
    race_indian = ndb.BooleanProperty()
    race_asian = ndb.BooleanProperty()
    race_african = ndb.BooleanProperty()
    race_hawaiian= ndb.BooleanProperty()
    race_white = ndb.BooleanProperty()
    ethnicity_indian = ndb.BooleanProperty()
    ethnicity_asian = ndb.BooleanProperty()
    ethnicity_african = ndb.BooleanProperty()
    ethnicity_hawaiian= ndb.BooleanProperty()
    ethnicity_white = ndb.BooleanProperty()
    industry = ndb.StringProperty()
    income = ndb.StringProperty()
    sex_orient = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zip_code = ndb.StringProperty()
    email = ndb.StringProperty()
