from flask import Flask
from flask_pymongo import PyMongo

#https://flask-pymongo.readthedocs.io/en/latest/
app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)

from app.controllers import default