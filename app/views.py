from flask import Blueprint, render_template, redirect, request, session
from flask.views import MethodView
from requests import get, put, post, delete
from requests.auth import HTTPBasicAuth

movies = Blueprint('movies', __name__, template_folder='templates')
API_HOST = "http://localhost:5001/api/v1/{endpoint}"

class Movies(MethodView):

    def login(self):
        return render_template('login.html',
                               title = 'Home')

    def validate_login(self):
        args = request.form
        session['username'], session['password'] = args.get('username', None), args.get('password', None)
        next = args.get('next_url', None)
        if next:
            return redirect('/movies', code=302)
        else:
            return redirect('/movies', code=302)


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
        username = session.get('username', '')
        password = session.get('password', '')
        response = delete('http://localhost:5001/api/v1/movie/{}'.format(slug), auth=HTTPBasicAuth(username, password))

        if response.status_code == 401:
            return redirect('/login', code=302)
        else:
            return redirect('/movies', code=302)

    def edit_movie(self, slug):
        movie = get('http://localhost:5001/api/v1/movie/{}'.format(slug)).json()
        return render_template('movies/edit_movie.html',
                               title = 'Home',
                               movie=movie)

    def save_movie(self):
        movie = request.form
        slug = movie.get('slug', None)
        if slug:
            post('http://localhost:5001/api/v1/movie/{}'.format(movie['slug']), data=movie).json()
        else:
            put('http://localhost:5001/api/v1/movie/new', data=movie).json()

        return redirect('/movies', code=302)

    def add_new_movie(self):
        return render_template('movies/add_movie.html',
                               title = 'Home')


# Register the urls
movies.add_url_rule('/login/', view_func=Movies().login)
movies.add_url_rule('/login/validate/', view_func=Movies().validate_login, methods=['POST'])
movies.add_url_rule('/movies/', view_func=Movies.as_view('list'))
movies.add_url_rule('/movies/<slug>', view_func=Movies().get_a_movie)
movies.add_url_rule('/movies/delete/<slug>', view_func=Movies().delete_movie)
movies.add_url_rule('/movies/edit/<slug>', view_func=Movies().edit_movie)
movies.add_url_rule('/movies/save/', view_func=Movies().save_movie, methods=['POST'])
movies.add_url_rule('/movies/add/', view_func=Movies().add_new_movie)