from api import mongo
from slugify import slugify
import re


class Movies():

    @classmethod
    def all(self):
        """
        Returns all movies
        """
        movies = mongo.db.movies.find()
        return movies

    @staticmethod
    def get(movie_slug):
        """
        Returns a specific movie with slug = movie_slug
        :params movie_slug (String) Slug of the requested movie
        """
        movie = mongo.db.movies.find_one( { 'slug': movie_slug } )

        if movie: return movie
        else: return {}

    @staticmethod
    def add(**kwargs):
        """
        Adds a new movie

        """
        kwargs = Movies.sanitize_insert_arguments(**kwargs)
        if Movies.can_add_movie(**kwargs):
            mongo.db.movies.insert( kwargs )
            return {'success': True}
        else:
            return {'success': False, 'errMsg': 'Movie name already exists'}

    @staticmethod
    def delete(movie_slug):
        mongo.db.movies.remove( {'slug': movie_slug} )
        return {'success': True}

    @staticmethod
    def update(movie_slug, **args):
        mongo.db.movies.update( {'slug': movie_slug}, {'$set': args}, upsert=False, multi=False )
        return {'success': True}

    @staticmethod
    def search(query):
        tokens = Movies.parse_search_tokens(query)
        all_movies = []
        for token in tokens:
            movies = mongo.db.movies.find( { '$or' :
                                                           [
                                                               {'name':token},
                                                               {'genre':token},
                                                               {'director': token}
                                                           ]
            } )
            all_movies += movies

        return all_movies


    @staticmethod
    def parse_search_tokens(tokens):
        queries = tokens.split(' ')
        regexes = []
        for query in queries:
            regex = ".*" + query + ".*"
            regexes.append( re.compile(regex, re.IGNORECASE) )

        return regexes

    @staticmethod
    def object_exists(object):
        return object.count() > 0

    @staticmethod
    def sanitize_insert_arguments(**kwargs):
        name = kwargs.get('name', None)
        if not name: raise Exception('Name of the movie is compulsory')
        kwargs['slug'] = slugify(unicode(name))

        return kwargs

    @staticmethod
    def can_add_movie(**kwargs):
        movie = mongo.db.movies.find_one( {'slug': kwargs.get('slug', '') } )
        if movie:
            return False
        else:
            return True
