from flask.views import View
from flask import render_template


class Checkout(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('checkout.html')


class Confirmation(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('confirmation.html')