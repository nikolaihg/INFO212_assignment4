import neo4j
from db import driver, node_to_json
from db_utils import DatabaseSession  # Importing our DatabaseSession context manager

class CarModel:
    def __init__(self, driver, make=None, model=None, year=None, location=None, status=None):
        self.driver = driver
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        self.status = status

    def post_sample_cars(self):
        query = """
        CREATE (car1:Car {car_id: 1, make: 'Toyota', model: 'Corolla', year: 2020, location: 'Location A', status: 'available'})
        CREATE (car2:Car {car_id: 2, make: 'Honda', model: 'Civic', year: 2021, location: 'Location B', status: 'available'})
        CREATE (car3:Car {car_id: 3, make: 'Ford', model: 'Focus', year: 2019, location: 'Location C', status: 'available'})
        """
        return self.execute_query(query)

    def create_car(self, car_id, make, model, year, location, status):
        query = """
        CREATE (car:Car {car_id: $car_id make: $make, model: $model, year: $year, location: $location, status: $status})
        RETURN car
        """
        return self.execute_query(query, {"car_id": car_id, "make": make, "model": model, "year": year, "location": location, "status": status})
    
    def read_car(self, car_id):
        query = "MATCH (car:Car) WHERE car.car_id = $car_id RETURN car"
        return self.execute_query(query, {"car_id": car_id})

    def update_car(self, car_id, **kwargs):
        set_clause = ", ".join([f"car.{key} = ${key}" for key in kwargs])
        query = f"MATCH (car:Car) WHERE car.car_id = $car_id SET {set_clause} RETURN car"
        kwargs["car_id"] = car_id
        return self.execute_query(query, kwargs)
    
    def order_car(self, car_id, customer_id):
            query ="MATCH (c:Customer {customer_id: $customer_id}), (car:Car {car_id: $car_id}) WHERE NOT (c)-[:BOOKED]->(:Car) AND car.status = 'available' MERGE (c)-[:BOOKED]->(car) SET car.status = 'booked' RETURN c, car"
            return self.execute_query(query, {"car_id": car_id, "customer_id": customer_id})
    
    def cancel_order_car(self, customer_id, car_id):
            query = "MATCH (c:Customer {customer_id: $customer_id}), (car:Car {car_id: $car_id}),(c)-[r:BOOKED]->(car) SET car.status = 'available' DELETE r RETURN c, car"
            return self.execute_query(query, {"car_id": car_id, "customer_id": customer_id})
    
    def rent_car(self, customer_id, car_id):
            query = "MATCH (c:Customer {customer_id: $customer_id})-[r:BOOKED]->(car:Car {car_id: $car_id}) SET car.status = 'rented'CREATE (c)-[:RENTED]->(car) DELETE r RETURN c, car"
            return self.execute_query(query, {"car_id": car_id, "customer_id": customer_id})

    def delete_car(self, car_id):
         query = "MATCH (car:Car) WHERE car.car_id = $car_id DELETE car"
         return self.execute_query(query, {"car_id": car_id})
    
    def return_car(self, customer_id, car_id, status):
          standard_query =  "MATCH (c:Customer {customer_id: $customer_id})-[r:RENTED]->(car:Car {car_id: $car_id}) SET car.status = 'available' DELETE r RETURN c, car" 
          damaged_query = "MATCH (c:Customer {customer_id: $customer_id})-[r:RENTED]->(car:Car {car_id: $car_id}) SET car.status = 'damaged' DELETE r RETURN c, car"
          if status == "damaged":
               return self.execute_query(damaged_query)
          elif status == "rented": 
             return self.execute_query(standard_query, {"customer_id": customer_id, "car_id": car_id, "status": status})
          else: 
                return {"error": "Invalid status provided for the return operation."}
    
    def return_car(self, customer_id, car_id, status):
          standard_query =  "MATCH (c:Customer {customer_id: $customer_id})-[r:RENTED]->(car:Car {car_id: $car_id}) SET car.status = 'available' DELETE r RETURN c, car" 
          damaged_query = "MATCH (c:Customer {customer_id: $customer_id})-[r:RENTED]->(car:Car {car_id: $car_id}) SET car.status = 'damaged' DELETE r RETURN c, car"
          if status == "damaged":
               return self.execute_query(damaged_query)
          elif status == "rented": 
             return self.execute_query(standard_query, {"customer_id": customer_id, "car_id": car_id, "status": status})
          else: 
                return {"error": "Invalid status provided for the return operation."}
    
    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            
            # List to store JSON-converted nodes
            nodes_json = []
            
            # Process each record in the result
            for record in result:
                record_json = {}
                
                # Convert each node in the record (if present) to JSON
                for key, value in record.items():
                    if isinstance(value, neo4j.graph.Node):
                        record_json[key] = node_to_json(value)
                
                # Only add to nodes_json if there's something in record_json
                if record_json:
                    nodes_json.append(record_json)
                    
            return nodes_json if nodes_json else None
