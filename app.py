from flask import Flask
from neo4j import GraphDatabase
from dotenv import load_dotenv
from config import Config
from models import CarModel, CustomerModel, EmployeeModel  # Import from `models` package
from api import api_bp


# Load environment variables
load_dotenv()

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

# Define routes (using the previously created Blueprint setup)
app.register_blueprint(api_bp, url_prefix='/api')


# Run the app
if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
