from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
from neo4j.exceptions import ServiceUnavailable, AuthError, Neo4jError
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Config:
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Check if the variables are loaded correctly
print(f"NEO4J_URI: {Config.NEO4J_URI}")
print(f"NEO4J_USERNAME: {Config.NEO4J_USERNAME}")
print(f"NEO4J_USERNAME: {Config.NEO4J_PASSWORD}")

# Initializing the driver
try:
    driver = GraphDatabase.driver(Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD))
    # Optional connection test to verify immediately
    with driver.session() as session:
        session.run("RETURN 1")
    print("Connection established successfully.")
except AuthError:
    print("Authentication error: Check your username or password.")
except ServiceUnavailable:
    print("Service unavailable: Verify that Neo4j is running and accessible.")
except Neo4jError as e:
    print(f"Neo4j error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

def db_session():
    try:
        return driver.session()
    except Exception as e:
        print(f"Error creating session: {e}")
        return None
    
def close_db():
    if driver:
        driver.close()
        print("Database connection closed.")

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

def node_to_dict(node):
    return node(dict)