from flask import Flask, request, jsonify
from routes.car_routes import car_bp
from dotenv import load_dotenv
from models import CarModel, CustomerModel, EmployeeModel
from api import api_bp
from db import driver  # Use the driver from db.py
import os

app.register_blueprint(car_bp, url_prefix='/cars')

if __name__ == '__main__':
    app.run(debug=True)

# Load environment variables
load_dotenv()

class Config:
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    DEBUG = True  # or False, as needed

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate models
car_model = CarModel(driver)
customer_model = CustomerModel(driver)
employee_model = EmployeeModel(driver)

# Root route for "API is running" message
@app.route('/')
def index():
    return "<h1>API is running</h1>"

# Register the main API blueprint
app.register_blueprint(api_bp, url_prefix='/api')

# Ensure the driver closes when the app stops
@app.teardown_appcontext
def close_driver(exception=None):
    if driver:
        driver.close()

# Run the app
if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])

