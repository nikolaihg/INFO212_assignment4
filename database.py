from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve Neo4j connection details from environment variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


# Neo4j connection setup using the credentials from .env file
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    print("Neo4j connected successfully")
except Exception as e:
    print(f"Error connecting to Neo4j: {e}")

def execute_query(query, parameters=None):
    with driver.session() as session:
        return session.run(query, parameters)
    
from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self._driver = GraphDatabase.driver(uri, auth=(user, pwd))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]
