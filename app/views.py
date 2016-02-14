from flask import render_template, url_for, redirect, g
from flask.ext.github import GitHub
from app import app,github

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/authorize')
def auth():
    return github.authorize(scope='user,repo')
