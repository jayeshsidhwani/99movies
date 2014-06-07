from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from requests import get, post, put, delete

movies = Blueprint('movies', __name__, template_folder='templates')


class Movies(MethodView):

    def get(self):
        all_movies = get('http://localhost:5001/movies')
        return render_template('movies/all.html', movies=all_movies)

# class DetailView(MethodView):
#
#     form = model_form(Comment, exclude=['created_at'])
#
#     def get_context(self, slug):
#         post = Post.objects.get_or_404(slug=slug)
#         form = self.form(request.form)
#
#         context = {
#             "post": post,
#             "form": form
#         }
#         return context
#
#     def get(self, slug):
#         context = self.get_context(slug)
#         return render_template('posts/detail.html', **context)
#
#     def post(self, slug):
#         context = self.get_context(slug)
#         form = context.get('form')
#
#         if form.validate():
#             comment = Comment()
#             form.populate_obj(comment)
#
#             post = context.get('post')
#             post.comments.append(comment)
#             post.save()
#
#             return redirect(url_for('posts.detail', slug=slug))
#         return render_template('posts/detail.html', **context)


# Register the urls
movies.add_url_rule('/', view_func=Movies)