# INFO212_assignment4

# Car Rental System

## Overview
A Flask-based application using Neo4j for managing a car rental service, including CRUD operations for cars, customers, employees, and managing rental transactions.

## Setup

## 1. requirements:
```text
Flask==2.0.3
neo4j==4.4.0
python-dotenv==1.0.1
```

## 2. Create the .env file

In the root directory of your project (where app.py is located), create a .env file and add your Neo4j connection details: 

```text
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

## 3. Run the flask app
Run this command in the root directory:

```bash
flask run --debug
```

## 4. API Postman Collection
In this folder there are example JSON payloads, You can copy and paste each JSON example into a new request within Postman.

Or 

## Instructions for Importing the Collection

    Save the JSON provided as CarAPICollection.json.
    Open Postman and go to the Collections tab.
    Import the JSON file by clicking on Import and selecting:
     ```CarAPICollection.json``` / ``CustomerAPICollection.json``` / ```EmployeeAPICollection.json``` / ```OrderAPICollection.json```
    The collection with the requests specified for each controller and model should appear in Postman.

## Using the Collection

    Start your Flask application on http://localhost:5000.
    Use the imported requests in Postman to interact with the API. Adjust IDs and data as needed based on your database's records.