from neo4j import GraphDatabase
from db import driver
from db_utils import DatabaseSession  # Importing our DatabaseSession context manager

class EmployeeModel:
    def __init__(self, driver):
        self.driver = driver

    def create_sample_employees(self):
        query = """
        CREATE (employee1:Employee {name: 'Bob Williams', address: 'Branch A, City X', branch: 'Branch A'})
        CREATE (employee2:Employee {name: 'Sara Brown', address: 'Branch B, City Y', branch: 'Branch B'})
        CREATE (employee3:Employee {name: 'Tom Clark', address: 'Branch C, City Z', branch: 'Branch C'})
        """
        return self.execute_query(query)

    def create_employee(self, name, address, branch):
        query = """
        CREATE (employee:Employee {name: $name, address: $address, branch: $branch})
        RETURN employee
        """
        return self.execute_query(query, {"name": name, "address": address, "branch": branch})

    # Additional CRUD operations here

    def execute_query(self, query, parameters=None, dry_run=True):
        with DatabaseSession(self.driver, dry_run=dry_run) as session:
            result = session.run(query, parameters)
            return result.single() if result else None
