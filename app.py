from flask import Flask, request, jsonify
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve Neo4j connection details from environment variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Initialize the Flask app
app = Flask(__name__)

# Neo4j connection setup using the credentials from .env file
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    print("Neo4j connected successfully")
except Exception as e:
    print(f"Error connecting to Neo4j: {e}")

def execute_query(query, parameters=None):
    with driver.session() as session:
        return session.run(query, parameters)

@app.route('/')
def home():
    return "Car Rental API is running"

# Your other routes and logic here

# Sample route to create a car
# @app.route('/create-car', methods=['POST'])
# def create_car():
#     data = request.json  # This was causing the error because request wasn't imported
#     query = """
#     CREATE (c:Car {make: $make, model: $model, year: $year, status: 'available'})
#     RETURN c
#     """
#     parameters = {
#         "make": data['make'],
#         "model": data['model'],
#         "year": data['year']
#     }
#     result = execute_query(query, parameters)
#     
#     return jsonify({"message": "Car created successfully!", "car": result.single()[0]}), 201

## @app.route('/create-car', methods=['POST'])
## def create_car():
##     # Temporarily bypass database to test
##     return jsonify({"message": "Car creation endpoint hit"}), 201

# Sample route to create a car
@app.route('/create-car', methods=['POST'])
def create_car():
    try:
        data = request.json  # Get the JSON data from the request
        query = """
        CREATE (c:Car {make: $make, model: $model, year: $year, status: 'available'})
        RETURN c
        """
        parameters = {
            "make": data['make'],
            "model": data['model'],
            "year": data['year']
        }
        
        result = execute_query(query, parameters)

        # Get the single record from the result
        car_node = result.single()
        if car_node is None:
            return jsonify({"error": "Car creation failed!"}), 500

        # Return success message and created car data
        return jsonify({"message": "Car created successfully!", "car": dict(car_node[0])}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)