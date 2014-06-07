from api import mongo
from actors import Actors
from bson.objectid import ObjectId

class Movies():

    @classmethod
    def all(self):
        movies = mongo.db.movies.find()
        return movies

    @staticmethod
    def get(movie_id):
        movie = mongo.db.movies.find( { '_id': ObjectId(movie_id) } )

        if Movies.object_exists(movie):
            return movie[0]
        else:
            return {}

    @staticmethod
    def add(**kwargs):
        male_lead = kwargs.get('male_lead_actor', None)
        if male_lead:
            kwargs['male_lead_actor'] = Actors.get_or_create( name = male_lead )['_id']

        movie = mongo.db.movies.insert( kwargs )
        return movie.find()

    @staticmethod
    def delete(movie_id):
        pass

    @staticmethod
    def object_exists(object):
        return object.count() > 0