# from api import mongo
# from . import db_connection

class Movies():
    # db = Connection.connect()
    # db = db_connection
    db = None

    def all(self):
        pass

    @staticmethod
    def get(db, movie_id):
        return db.movies.find( { id: movie_id } )

    @staticmethod
    def add(db, **kwargs):
        import code; code.interact(local=locals())
        Movies.db.movies.add( kwargs )

    @staticmethod
    def delete(movie_id):
        pass

# class Connection():

    # @staticmethod
    # def connect():
        # return PyMongo(app)