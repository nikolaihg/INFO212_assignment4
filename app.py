from flask import Flask, request, jsonify
# from neo4j import GraphDatabase
from dotenv import load_dotenv
from models import CarModel, CustomerModel, EmployeeModel
from api import api_bp
from db import driver  # Use the driver from db.py
import os

# Load environment variables
load_dotenv()
#Hei
class Config:
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    DEBUG = True  # or False, as needed

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# # Initialize the Neo4j driver
# driver = GraphDatabase.driver(Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD))

# Instantiate models
car_model = CarModel(driver)
customer_model = CustomerModel(driver)
employee_model = EmployeeModel(driver)

# Root route for "API is running" message
@app.route('/')
def index():
    return "<h1>API is running</h1>"

# # Populate the database with sample data on startup
# @app.before_request
# def initialize_database():
#     print("Initializing database with sample data...")
#     car_model.create_sample_cars()
#     customer_model.create_sample_customers()
#     employee_model.create_sample_employees()
#     print("Database initialized with sample data.")

# # Endpoint to create a new car
# @app.route('/api/cars', methods=['POST'])
# def create_car():
#     data = request.json
#     make = data.get('make')
#     model = data.get('model')
#     year = data.get('year')
#     location = data.get('location')
#     status = data.get('status')
#     
#     # Create the car in the database
#     result = car_model.create_car(make, model, year, location, status)
#     return jsonify(result=result), 201

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
