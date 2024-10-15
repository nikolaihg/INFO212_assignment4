from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'