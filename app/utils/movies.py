from app import db_connection

class Movies():

    def all(self):
        pass

    @staticmethod
    def get(movie_id):
        return db_connection.movies.find( { id: movie_id } )

    @staticmethod
    def add(**kwargs):
        import code; code.interact(local=locals())
        db_connection.movies.add( kwargs )

    @staticmethod
    def delete(movie_id):
        pass