from flask import Flask,render_template
app = Flask(__name__)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)

@app.route('/')
def index():
    return render_template('/movies/movies.html')

@app.route('/movie/')
def movie():
    return render_template('/movies/movie.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)