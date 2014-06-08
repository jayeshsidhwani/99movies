__author__ = 'jay'

from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = '99movies'

mongo = PyMongo(app)

VERSION = 'v1'

def register_blueprints(app):
    # Prevents circular imports
    from app.views import movies
    app.register_blueprint(movies)

register_blueprints(app)

if __name__ == '__main__':
    app.run()