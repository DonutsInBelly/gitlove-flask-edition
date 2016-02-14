from flask import render_template, url_for, redirect, g
from flask.ext.github import GitHub
#from __init__ import app
from app import app,github

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/authorize')
def authorize():
    return github.authorize()

#@app.route('/github-callback')
#@github.authorized_handler
#def authorized(oauth_token):
    #next_url = request.args.get('next')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/test')
def test():
    return render_template('test.html')
