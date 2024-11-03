from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD)
)

print(f"NEO4J_URI: {Config.NEO4J_URI}")  # 
print(f"NEO4J_USERNAME: {Config.NEO4J_USERNAME}") 
print(f"NEO4J_USERNAME: {Config.NEO4J_PASSWORD}") 

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties