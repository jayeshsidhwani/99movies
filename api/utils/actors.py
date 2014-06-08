from api import mongo


class Actors():

    @staticmethod
    def get_or_create(**kwargs):
        actor = mongo.db.actors.find_one( kwargs )

        if actor:
            return actor
        else:
            new_actor_id = mongo.db.actors.insert( kwargs )
            return mongo.db.actors.find_one( {'_id': new_actor_id} )

    @staticmethod
    def get(actor_slug_name):
        return mongo.db.actors.find_one( {'slug': actor_slug_name} )
