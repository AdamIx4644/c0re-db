import requests
from flask import Flask, request, redirect, render_template, url_for



app = Flask(__name__)


@app.route('/')
def button():
    # Generate the OAuth2 URL to redirect the user to the Discord login page
    return "hello world"

if __name__ == '__main__':
    app.run(port=6950)
