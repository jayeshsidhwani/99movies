# from flask import Flask
from flask.ext.restful import reqparse, Resource
# from flask.ext.pymongo import PyMongo

from movies import Movies

from . import app, api

# app = Flask(__name__)
# api = Api(app)
# # db_connection = PyMongo(app)


class Movie(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.arguments = { 'name': str, 'male_lead_actor': str, 'female_lead_actor': str,
                           'supporting_actors': list, 'box_office_ratings': float, 'popularity_score': int }
        self.add_arguments()
        self.db = DB

    def get(self, movie_id):
        return Movies.get(self.db, movie_id)
    #
    def delete(self, movie_id):
        return Movies.delete(movie_id), 200

    def put(self, movie_id):
        args = self.parser.parse_args()
        movie = Movies.add(self.db, **args)
        return movie, 200

    def add_arguments(self):
        for field, field_type in self.arguments.items():
            self.parser.add_argument(field, type=field_type)

api.add_resource(Movie, '/movies/<string:movie_id>')

if __name__ == '__main__':
    app.run(debug=True)