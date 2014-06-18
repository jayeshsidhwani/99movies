import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import app, api, VERSION
from flask.ext.restful import reqparse, Resource
from api.utils.movies import Movies
from api.utils.tokens import Tokens
from flask import request
from bson.json_util import dumps
from cors_header import cors

import json, ast


def encode_response(response):
    return json.loads(dumps(response))

class MovieAPI(Resource):
    decorators = [cors]
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.prepare_parser()

    @cors
    def get(self, movie_slug):
        response = Movies.get(movie_slug)
        return encode_response(response), 200

    @cors
    def delete(self, movie_slug):
        token = request.query_string
        # cleanup of token until you send header data in DELETE from ng
        token = token.split('=')[-1].replace('%22', '')

        response = Movies.delete(movie_slug, token)
        if response['success']:
            return encode_response(response), 200
        else:
            return encode_response(response), 500

    @cors
    def put(self, movie_slug):
        data = ast.literal_eval(request.data)['data']
        response = Movies.add(**data)
        return encode_response(response), 200

    @cors
    def post(self, movie_slug):
        request_data = ast.literal_eval(request.data)
        data, token = request_data['data'], request_data['token']

        response = Movies.update(movie_slug, token, **data)
        if response['success']:
            return encode_response(response), 200
        else:
            return encode_response(response), 500

    @cors
    def options(self, movie_slug):
        request.headers.get('Access-Control-Request-Method')
        return 200

    def prepare_parser(self):
        self.arguments = { 'name': str, 'genre': str, 'director': str, 'imdb_score': str,
                           '99popularity': str }
        self.add_arguments()

    def add_arguments(self):
        for field, field_type in self.arguments.items():
            self.parser.add_argument(field, type=field_type)

class MovieListAPI(Resource):

    @cors
    def get(self):
        response = Movies.all()
        return encode_response(response), 200

class MovieSearchAPI(Resource):

    @cors
    def get(self, query):
        response = Movies.search(query)
        return encode_response(response), 200

class TokenAPI(Resource):

    @cors
    def post(self):
        data = ast.literal_eval(request.data)
        response = Tokens.generate(data['username'], data['password'])
        return encode_response(response), 200

    @cors
    def options(self):
        return 200

api.add_resource(MovieAPI, '/api/{}/movie/<string:movie_slug>/'.format(VERSION))
api.add_resource(MovieListAPI, '/api/{}/movies/'.format(VERSION))
api.add_resource(MovieSearchAPI, '/api/{}/movies/search/<string:query>'.format(VERSION))
api.add_resource(TokenAPI, '/api/{}/login/'.format(VERSION))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)