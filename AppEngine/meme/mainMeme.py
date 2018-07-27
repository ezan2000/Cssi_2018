import webapp2
import json
from google.appengine.api import urlfetch
import random
import jinja2
import urllib
templateLoader = jinja2.FileSystemLoader(searchpath = "./")
templateEnv = jinja2.Environment(loader = templateLoader)

class memePage(webapp2.RequestHandler):
    def get(self):

        link = 'https://api.imgflip.com/get_memes'

        result = urlfetch.fetch(link)
        results  = json.loads(result.content)
        # self.response.write(results)
        memeDict = {}
        memeDict = random.choice(results['data']['memes'])
        pic = memeDict['url']
        capId = memeDict['id']
        self.response.write("<img src = {url}> ".format(url = pic))
        self.response.write(pic)


class memeTemp(webapp2.RequestHandler):
    def get(self):

        link = 'https://api.imgflip.com/get_memes'

        result = urlfetch.fetch(link)
        results  = json.loads(result.content)
        # self.response.write(results)
        memeDict = {}
        memeDict = random.choice(results['data']['memes'])
        capId = memeDict['id']

        template = templateEnv.get_template("templates/meme.html")

        self.response.write(template.render({'memeDict': memeDict}))
        # self.response.write("<img src = {url}> ".format(url = pic))

    def post(self):

        capLink = 'https://api.imgflip.com/caption_image'


        capDict = {
            'template_id': self.request.get('hidden'),
            'username':  'SolaireOfAstoraOfTheSun',
            'password': 'praisethesun',
            'text0':self.request.get('user-first-ln'),
            'text1':self.request.get('user-second-ln'),
            }

        caption = urlfetch.fetch(
            url = capLink,
            payload = urllib.urlencode(capDict),
            method = urlfetch.POST,
            )

        picDict = json.loads(caption.content)
        #self.response.write(picDict)

        memeDict = picDict['data']

        #self.response.write(pic)

        user1 = self.request.get('user-first-ln')
        user2 = self.request.get('user-second-ln')
        meme = self.request.get('meme-type')
        template = templateEnv.get_template("templates/meme.html")

        self.response.write(template.render({'memeDict': memeDict}))
        #self.response.write("my post Handler - {m} {u1} {u2}".format(m=meme,u1=user1,u2=user2))

        #recipeBrowser(webapp2.RequestHandler):
#     def get(self):
#         template = templateEnv.get_template("template/recipies/].html")
#         # recipe = {ingredients: ['carrots'],["potatoes"]}
#         self.response.write(template.render(recipie))
app = webapp2.WSGIApplication([
('/',memePage),
("/memeTemp", memeTemp),
('/memeresult', memeTemp),
],debug = True)
