from api import mongo
from bson.objectid import ObjectId


class Actors():

    @staticmethod
    def get_or_create(**kwargs):
        actors = mongo.db.actors.find_one( kwargs )

        if actors.count() > 0:
            return actors['_id']
        else:
            return mongo.db.actors.insert( kwargs )

    @staticmethod
    def get(actor_id):
        return mongo.db.actors.find_one( {'_id': ObjectId(actor_id)} )
