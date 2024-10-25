from neo4j import GraphDatabase

class CustomerModel:
    def __init__(self, driver):
        self.driver = driver

    def create_sample_customers(self):
        query = """
        CREATE (customer1:Customer {name: 'John Doe', age: 30, address: '123 Main St, City A'})
        CREATE (customer2:Customer {name: 'Jane Smith', age: 25, address: '456 Elm St, City B'})
        CREATE (customer3:Customer {name: 'Alice Johnson', age: 40, address: '789 Oak St, City C'})
        """
        return self.execute_query(query)

    def create_customer(self, name, age, address):
        query = """
        CREATE (customer:Customer {name: $name, age: $age, address: $address})
        RETURN customer
        """
        return self.execute_query(query, {"name": name, "age": age, "address": address})

    # Additional CRUD operations here

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return result.single() if result else None
