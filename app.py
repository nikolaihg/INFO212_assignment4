from flask import Flask
from db import *
from models import *

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return "<h1>API is running</h1>"

# @app.teardown_appcontext
# def close_driver(exception=None):
#     if Driver:
#         Driver.close()

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)