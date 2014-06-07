import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
db_connection = PyMongo(app)
