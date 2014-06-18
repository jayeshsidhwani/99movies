__author__ = 'jay'

from flask import Flask

app = Flask(__name__)
app.config['MONGO_DBNAME'] = '99movies'
app.config["SECRET_KEY"] = "this_is_my_secret_key_which_should_be_secret!"

VERSION = 'v1'

# def register_blueprints(app):
#     # Prevents circular imports
#     from app.views import movies
#     app.register_blueprint(movies)

# register_blueprints(app)

if __name__ == '__main__':
    app.run()