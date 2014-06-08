from flask import Blueprint, render_template, redirect, request
from flask.views import MethodView
from requests import get, put, post, delete

movies = Blueprint('movies', __name__, template_folder='templates')
API_HOST = "http://localhost:5001/api/v1/{endpoint}"

class Movies(MethodView):

    def get(self):
        permissions = { 'admin': False, 'super_admin': False, 'user': True }
        movies = get(API_HOST.format(endpoint = 'movies')).json()

        return render_template('movies/all_movies.html',
                               title = 'Home',
                               permissions = permissions,
                               movies=movies)

    def get_a_movie(self, slug):
        permissions = { 'admin': False, 'super_admin': False, 'user': True }
        movie = get('http://localhost:5001/api/v1/movie/{}'.format(slug)).json()

        return render_template('movies/movie.html',
                               title = 'Home',
                               permissions = permissions,
                               movie=movie)

    def delete_movie(self, slug):
        permissions = { 'admin': False, 'super_admin': False, 'user': True }
        delete('http://localhost:5001/api/v1/movie/{}'.format(slug)).json()

        return redirect('/movies', code=302)

    def edit_movie(self, slug):
        movie = get('http://localhost:5001/api/v1/movie/{}'.format(slug)).json()
        return render_template('movies/edit_movie.html',
                               title = 'Home',
                               movie=movie)

    def save_movie(self):
        movie = request.form
        post('http://localhost:5001/api/v1/movie/{}'.format(movie['slug']), data=movie).json()

        return redirect('/movies', code=302)

# Register the urls
movies.add_url_rule('/movies/', view_func=Movies.as_view('list'))
movies.add_url_rule('/movies/<slug>', view_func=Movies().get_a_movie)
movies.add_url_rule('/movies/delete/<slug>', view_func=Movies().delete_movie)
movies.add_url_rule('/movies/edit/<slug>', view_func=Movies().edit_movie)
movies.add_url_rule('/movies/save/', view_func=Movies().save_movie, methods=['POST'])