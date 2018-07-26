import webapp2
import jinja2
import os
import time
from banking import Transaction

jinjaLoad = jinja2.FileSystemLoader('./')
jinjaDir = jinja2.Environment(loader = jinjaLoad, extensions = ["jinja2.ext.autoescape" ],
autoescape = True)
def get_balance():
    #get all transactions in our account
    transactions = Transaction.query().fetch()
    # add up the balance
    balance = 0
    for trans in transactions:
        #getting amount for every transaction in the data storage
        balance += trans.amount

    return balance


class BankingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinjaDir.get_template('Templates/banking.html')

        myDict = {'current_balance': get_balance()}
        self.response.write(template.render(myDict))


class moneyHandler(webapp2.RequestHandler):
    def post(self):
        template = jinjaDir.get_template('Templates/banking.html')
        amount = int(self.request.get('amount'))
        transaction = Transaction(amount = amount)
        transaction.put()
        time.sleep(1)


        myDict = {'current_balance': get_balance()}
        self.response.write(template.render(myDict))

bank = webapp2.WSGIApplication([
("/banking", BankingHandler),
('/money', moneyHandler)


],debug =True)
