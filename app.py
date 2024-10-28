from flask import Flask
from neo4j import GraphDatabase
from dotenv import load_dotenv
from models import CarModel, CustomerModel, EmployeeModel  # Import from `models` package
from api import api_bp
import os

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

# Initialize the Neo4j driver
driver = GraphDatabase.driver(Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD))

# Instantiate models
car_model = CarModel(driver)
customer_model = CustomerModel(driver)
employee_model = EmployeeModel(driver)

# Populate the database with sample data on startup
@app.before_first_request
def initialize_database():
    print("Initializing database with sample data...")
    car_model.create_sample_cars()
    customer_model.create_sample_customers()
    employee_model.create_sample_employees()
    print("Database initialized with sample data.")

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
