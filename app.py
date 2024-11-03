from flask import Flask, request, jsonify
from routes.car_routes import car_bp
from dotenv import load_dotenv
from models import CarModel, CustomerModel, EmployeeModel
from api import *
from db import *  # Use the driver from db.py
# from routes.car_routes import car_bp
# from routes.rental_routes import rental_bp
# from routes.customer_routes import customer_bp
# from routes.employee_routes import employee_bp
import os

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate models
car_model = CarModel(driver)
customer_model = CustomerModel(driver)
employee_model = EmployeeModel(driver)

@app.route('/')
def index():
    return "<h1>API is running</h1>"

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(car_bp, url_prefix='/cars') 
app.register_blueprint(rental_bp, url_prefix='/rentals')
app.register_blueprint(customer_bp, url_prefix = '/customers' )
app.register_blueprint(employee_bp, url_prefix = '/employees' )

# Ensure the driver closes when the app stops
@app.teardown_appcontext
def close_driver(exception=None):
    if driver:
        driver.close()

# Run the app
if __name__ == "__main__":
     app.run(debug=app.config['DEBUG'])
