__author__ = 'jay'

from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = '99movies'
mongo = PyMongo(app)

VERSION = 'v1'

if __name__ == '__main__':
    app.run()