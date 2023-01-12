from flask import Flask, request, redirect, render_template, url_for
from serverless_wsgi import WSGIApplication


app = Flask(__name__, static_folder='.')


@app.route('/')
def button():
    # Generate the OAuth2 URL to redirect the user to the Discord login page
    return "hello world"




wsgi_app = WSGIApplication(app)
