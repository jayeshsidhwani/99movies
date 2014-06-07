__author__ = 'jay'

from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
db_connection = PyMongo(app)