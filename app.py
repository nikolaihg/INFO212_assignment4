from flask import Flask, request, jsonify
from database import Config, db_session, close_db
from controllers.car_controller import car_blueprint

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(car_blueprint)

@app.route('/')
def index():
    return "<h1>API is running</h1>"

# app.register_blueprint(api_bp, url_prefix='/api')
# app.register_blueprint(car_bp, url_prefix='/cars') 
# app.register_blueprint(rental_bp, url_prefix='/rentals')
# app.register_blueprint(customer_bp, url_prefix = '/customers' )
# app.register_blueprint(employee_bp, url_prefix = '/employees' )

# Ensure the driver closes when the app stops
@app.teardown_appcontext
def close_driver(exception=None):
    close_db()

# Run the app
if __name__ == "__main__":
     app.run(debug=app.config['DEBUG'])
