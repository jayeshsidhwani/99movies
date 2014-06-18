__author__ = 'jay'

from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Api

app = Flask(__name__)
app.config['MONGO_DBNAME'] = '99movies'
# app.config['MONGO_URI'] = 'mongodb://jayesh:jayesh@kahana.mongohq.com:10008/99movies'
api = Api(app)
mongo = PyMongo(app)

VERSION = 'v1'