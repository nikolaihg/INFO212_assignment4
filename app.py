from flask import Flask
from routes.api import api_blueprint

app = Flask(__name__)

# Register the blueprint for API routes
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
