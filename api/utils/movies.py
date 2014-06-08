from api import mongo
from actors import Actors
from slugify import slugify

class Movies():

    @classmethod
    def all(self):
        movies = mongo.db.movies.find()
        return movies

    @staticmethod
    def get(movie_slug):
        movie = mongo.db.movies.find_one( { 'slug': movie_slug } )

        if movie: return movie
        else: return {}

    @staticmethod
    def add(**kwargs):
        kwargs = Movies.sanitize_insert_arguments(**kwargs)
        if Movies.can_add_movie(**kwargs):
            mongo.db.movies.insert( kwargs )
            return {'success': True}
        else:
            return {'success': False, 'errMsg': 'Movie name already exists'}

    @staticmethod
    def delete(movie_id):
        pass

    @staticmethod
    def object_exists(object):
        return object.count() > 0

    @staticmethod
    def sanitize_insert_arguments(**kwargs):

        name = kwargs.get('name', None)
        if not name: raise Exception('Name of the movie is compulsory')
        kwargs['slug'] = slugify(name)

        for actor in ['male_lead_actor', 'female_lead_actor']:
            _actor_name = kwargs.get(actor, None)
            if _actor_name:
                _actor_name_slug = slugify(_actor_name)
                kwargs[actor] = Actors.get_or_create( slug = _actor_name_slug,
                                                      name = _actor_name )['slug']
        return kwargs

    @staticmethod
    def can_add_movie(**kwargs):
        movie = mongo.db.movies.find_one( {'slug': kwargs.get('slug', '') } )
        if movie:
            return False
        else:
            return True
