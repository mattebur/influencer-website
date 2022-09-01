from influencer import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/twitter')
def twitter_page():
    return render_template('twitter.html')


@app.route('/gmail')
def gmail_page():
    return render_template('gmail.html')