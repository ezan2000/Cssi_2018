import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('lail is dumb')

app = webapp2.WSGIApplication([

('/hello', MainHandler),
], debug =True)
