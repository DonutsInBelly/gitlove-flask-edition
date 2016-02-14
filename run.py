#!venv/bin/python
from flask import Flask, render_template
from app import app,views

app.run(debug=True)

