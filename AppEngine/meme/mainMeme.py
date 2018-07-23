import webapp2
import json
from google.appengine.api import urlfetch

class memePage(webapp2.RequestHandler):
    def get(self):

        link = 'https://api.imgflip.com/get_memes'

        result = urlfetch.fetch(link)
        results  = json.loads(result.content)


        self.response.write("<img src = {url}/> ".format(url = result))
        self.response.write("wow")

app = webapp2.WSGIApplication([
('/',memePage)

],debug = True)
