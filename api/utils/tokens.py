import binascii, os
from api import mongo

class Tokens():

    @classmethod
    def generate(cls, username, password):
        type = cls.resolve_type_of_user(username, password)
        token = binascii.hexlify(os.urandom(16))
        mongo.db.tokens.insert( {'token': token, 'type': type})
        return token

    @classmethod
    def resolve_type_of_user(cls, username, password):
        if (password == 'admin'):
            return 'admin'
        elif (password == 'super_admin'):
            return 'super_admin'
        else:
            return 'normal'