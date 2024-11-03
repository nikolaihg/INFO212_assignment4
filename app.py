from flask import Flask
from dotenv import load_dotenv
from models import CarModel, CustomerModel, EmployeeModel
from api import api_bp
from db import driver  # Use the driver from db.py
from config import Config

# Load environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate models with Neo4j driver from db.py
car_model = CarModel(driver)
customer_model = CustomerModel(driver)
employee_model = EmployeeModel(driver)

# Root route to check API status
@app.route('/')
def index():
    return "<h1>API is running</h1>"

# Optional: Initialize the database with sample data on startup
# Uncomment if needed
# @app.before_first_request
# def initialize_database():
#     car_model.create_sample_cars()
#     customer_model.create_sample_customers()
#     employee_model.create_sample_employees()

# Register the main API blueprint
app.register_blueprint(api_bp, url_prefix='/api')

# Ensure the driver closes when the app stops
@app.teardown_appcontext
def close_driver(exception=None):
    if driver:
        driver.close()

# Run the app
if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
