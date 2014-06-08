import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import app, api, VERSION
from flask.ext.restful import reqparse, Resource
from api.utils.movies import Movies
from api.utils.actors import Actors
from api.auth import requires_auth
from bson.json_util import dumps
import json


def encode_response(response):
    return json.loads(dumps(response))

class MovieAPI(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.prepare_parser()

    def get(self, movie_slug):
        response = Movies.get(movie_slug)
        return encode_response(response), 200

    @requires_auth
    def delete(self, movie_slug):
        return Movies.delete(movie_slug), 200

    def put(self, movie_slug):
        args = self.parser.parse_args()
        response = Movies.add(**args)
        return encode_response(response), 200

    def post(self, movie_slug):
        args = self.parser.parse_args()
        response = Movies.update(movie_slug, **args)
        return encode_response(response), 200

    def prepare_parser(self):
        self.arguments = { 'name': str, 'male_lead_actor': str, 'female_lead_actor': str,
                           'director': str, 'imdb_score': float, '99popularity': int }
        self.add_arguments()

    def add_arguments(self):
        for field, field_type in self.arguments.items():
            self.parser.add_argument(field, type=field_type)

class MovieListAPI(Resource):

    def get(self):
        response = Movies.all()
        return encode_response(response), 200

class ActorAPI(Resource):
    def get(self, actor_id):
        response = Actors.get(actor_id)
        return encode_response(response), 200

api.add_resource(MovieAPI, '/api/{}/movie/<string:movie_slug>'.format(VERSION))
api.add_resource(MovieListAPI, '/api/{}/movies/'.format(VERSION))
api.add_resource(ActorAPI, '/api/{}/actor/<string:actor_id>'.format(VERSION))

if __name__ == '__main__':
    app.run(debug=True, port=5001)