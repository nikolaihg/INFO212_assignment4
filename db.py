from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class Config:
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Check if the variables are loaded correctly
print(f"NEO4J_URI: {Config.NEO4J_URI}")  # Debugging line to check the URI
print(f"NEO4J_USERNAME: {Config.NEO4J_USERNAME}")  # Debugging line

print("NEO4J_URI:", Config.NEO4J_URI)
print("NEO4J_USERNAME:", Config.NEO4J_USERNAME)
print("NEO4J_PASSWORD:", Config.NEO4J_PASSWORD)

driver = GraphDatabase.driver(
    Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD)
)