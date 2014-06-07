import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import app, api, VERSION
from flask.ext.restful import reqparse, Resource
from api.utils.movies import Movies
from api.utils.actors import Actors
from bson.json_util import dumps
import json


def encode_response(response):
    return json.loads(dumps(response))

class MovieAPI(Resource):

    def __init__(self):
        self.argument_parser = reqparse.RequestParser()

    def get(self, movie_id):
        response = Movies.get(movie_id)
        return encode_response(response), 200

    def delete(self, movie_id):
        return Movies.delete(movie_id), 200

    def put(self):
        args = self.parser.parse_args()
        response = Movies.add(**args)
        return encode_response(response), 200

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

class MovieListAPI(Resource):

    def get(self):
        response = Movies.all()
        return encode_response(response), 200

class ActorAPI(Resource):
    def get(self, actor_id):
        response = Actors.get(actor_id)
        return encode_response(response), 200

api.add_resource(MovieAPI, '/api/{}/movie/<string:movie_id>'.format(VERSION))
api.add_resource(MovieListAPI, '/api/{}/movies/'.format(VERSION))
api.add_resource(ActorAPI, '/api/{}/actor/<string:actor_id>'.format(VERSION))

if __name__ == '__main__':
    app.run(debug=True, port=5001)