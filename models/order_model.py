# from neo4j import GraphDatabase
from db import driver
class CustomerModel:
    def __init__(self, driver):
        self.driver = driver

    def order_car(self, customer_id, car_id):
        query = """
        MATCH (customer:Customer, (car:Car)
        WHERE ID(customer) = $customer_id andID(car) = $car_id
        CREATE (customer)-[:ORDERED]->(car)
        RETURN customer, car
        """
        with self.driver.session() as session:
            result = session.run(query, customer_id=customer_id, car_id=car_id)
            return result.single() if result else None
