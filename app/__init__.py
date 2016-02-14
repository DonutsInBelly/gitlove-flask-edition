#!venv/bin/python
from flask import Flask
from flask.ext.github import GitHub

app = Flask(__name__)
app.config.from_pyfile('../config.py')

github = GitHub(app)

from app import views
