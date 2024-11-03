from neo4j import GraphDatabase
from db import driver
from db_utils import DatabaseSession  # Importing our DatabaseSession context manager

class CustomerModel:
    def __init__(self, driver):
        self.driver = driver

    def create_sample_customers(self):
        query = """
        CREATE (customer1:Customer {customer_id: 1, name: 'John Doe', age: 30, address: '123 Main St, City A'})
        CREATE (customer2:Customer {customer_id: 2, name: 'Jane Smith', age: 25, address: '456 Elm St, City B'})
        CREATE (customer3:Customer {customer_id: 3, name: 'Alice Johnson', age: 40, address: '789 Oak St, City C'})
        """
        return self.execute_query(query)

    def create_customer(self, customer_id, name, age, address):
        query = """
        CREATE (customer:Customer {customer_id: $customer_id, name: $name, age: $age, address: $address})
        RETURN customer
        """
        return self.execute_query(query, {"customer_id": customer_id, "name": name, "age": age, "address": address})

    # Additional CRUD operations here

    def execute_query(self, query, parameters=None, dry_run=True):
        with DatabaseSession(self.driver, dry_run=dry_run) as session:
            result = session.run(query, parameters)
            return result.single() if result else None