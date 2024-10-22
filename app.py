from flask import Flask
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
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

def execute_query(query, parameters=None):
    with driver.session() as session:
        return session.run(query, parameters)

@app.route('/')
def home():
    return "Car Rental API is running"

# Your other routes and logic here

if __name__ == "__main__":
    app.run(debug=True)