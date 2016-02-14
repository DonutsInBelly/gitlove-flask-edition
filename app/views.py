from flask import render_template, url_for, redirect, g
from flask.ext.github import GitHub
#from __init__ import app
from app import app,github

import requests, json

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/authorize')
def authorize():
    return github.authorize()

@app.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    url = 'https://api.github.com/user?access_token={0}'.format(oauth_token)
    myResponse1 = requests.get(url)
    myRepos = json.loads(myResponse1._content).get('repos_url')
    myReponse2 = requests.get(myRepos)
    theRepos = json.loads(myReponse2._content)
    j = theRepos[0].get('language')
    myLanguages = {}
    for aRepo in theRepos:
        if myLanguages.has_key(aRepo.get('language')):
            myLanguages[aRepo.get('language')] += 1 #
        else:
            myLanguages[aRepo.get('language')] = 1 #adding it to a dictionary if not there
    print myLanguages
    print findMatch('Java')
    #
    return j
    #repourl = 'https://api.github.com/users/{0}/repos'.format(username)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/test')
def test():
    return render_template('test.html')

def findMatch(lang):
	nameList = []
	pubRepos = 'https://api.github.com/repositories'
	pubRepoRes = requests.get(pubRepos)
	fileJson = json.loads(pubRepoRes._content)
	for repo in fileJson:
		resObj = repo.get('languages_url')
		res = requests.get(resObj)
    	resJson = json.loads(res._content) #languages url
    	loginName = repo.get('owner').get('login')
    	print loginName
    	if(resJson.has_key(lang)):
    		nameList.append(loginName)
    	print nameList
    	return nameList







