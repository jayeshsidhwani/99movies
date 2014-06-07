import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, api

from flask.ext.restful import reqparse, Resource
from app.utils.movies import Movies


class Movie(Resource):

    def __init__(self):
        self.argument_parser = reqparse.RequestParser()

    def get(self, movie_id):
        return Movies.get(movie_id)

    def delete(self, movie_id):
        return Movies.delete(movie_id), 200

    def put(self, movie_id):
        args = self.parser.parse_args()
        movie = Movies.add(**args)
        return movie, 200

    def add_arguments(self):
        for field, field_type in self.arguments.items():
            self.parser.add_argument(field, type=field_type)

    @property
    def argument_parser(self):
        return self.parser

    @argument_parser.setter
    def argument_parser(self, parse):
        self.parser = parse
        self.arguments = { 'name': str, 'male_lead_actor': str, 'female_lead_actor': str,
                           'supporting_actors': list, 'box_office_ratings': float, 'popularity_score': int }
        self.add_arguments()

api.add_resource(Movie, '/movies/<string:movie_id>')

if __name__ == '__main__':
    app.run(debug=True)