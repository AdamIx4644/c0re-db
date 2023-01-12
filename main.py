import requests
from flask import Flask, request, redirect, render_template, url_for



app = Flask(__name__, static_folder='.')


@app.route('/')
def button():
    # Generate the OAuth2 URL to redirect the user to the Discord login page
    return render_template('index.html', members="2016", servers="23")




if __name__ == '__main__':
    app.run(port=6969)
