from google.appengine.ext import ndb
"""

"""

class Movie(ndb.Model):


    title = ndb.StringProperty(required = True, default = 'Bill and Ted')
    media_type = ndb.StringProperty(required = True, default = "movie")
    runtime = ndb.IntegerProperty(required = False)
    rating = ndb.FloatProperty(required = False)



class User(ndb.Model):

    userName = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = True)
