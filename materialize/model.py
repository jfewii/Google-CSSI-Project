# import webapp2
#
# from google.appengine.ext import ndb
#
# class CssiUser(ndb.Model):
#   first_name = ndb.StringProperty()
#   last_name = ndb.StringProperty()
#   email = ndb.StringProperty()

from google.appengine.ext import ndb

class UserDataStore(ndb.Model):
    username = ndb.StringProperty()
    psw = ndb.StringProperty()

class ProfileStore(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    age = ndb.StringProperty()
    gender = ndb.StringProperty()
    

    industry = ndb.StringProperty()
    income = ndb.StringProperty()
    sex_orient = ndb.StringProperty()
    city = ndb.StringProperty()

    zip_code = ndb.StringProperty()

    def get_profile_info(self):
        return "hello " + self.first_name + " " + self.last_name
>>>>>>> 8bfb283948d30462d6c83c1e23e2ac8d0fb8718f
