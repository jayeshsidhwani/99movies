__author__ = 'jay'

from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Api

app = Flask(__name__)
app.config['MONGO_DBNAME'] = '99movies'
api = Api(app)
mongo = PyMongo(app)

VERSION = 'v1'