from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/movies/all.html')

@app.route('/login')
def login():
    return render_template('/login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)