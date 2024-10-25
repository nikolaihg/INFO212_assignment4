from neo4j import GraphDatabase

class CarModel:
    def __init__(self, driver):
        self.driver = driver

    def create_sample_cars(self):
        query = """
        CREATE (car1:Car {make: 'Toyota', model: 'Corolla', year: 2020, location: 'Location A', status: 'available'})
        CREATE (car2:Car {make: 'Honda', model: 'Civic', year: 2021, location: 'Location B', status: 'available'})
        CREATE (car3:Car {make: 'Ford', model: 'Focus', year: 2019, location: 'Location C', status: 'available'})
        """
        return self.execute_query(query)

    def create_car(self, make, model, year, location, status):
        query = """
        CREATE (car:Car {make: $make, model: $model, year: $year, location: $location, status: $status})
        RETURN car
        """
        return self.execute_query(query, {"make": make, "model": model, "year": year, "location": location, "status": status})

    def read_car(self, car_id):
        query = "MATCH (car:Car) WHERE ID(car) = $car_id RETURN car"
        return self.execute_query(query, {"car_id": car_id})

    def update_car(self, car_id, **kwargs):
        set_clause = ", ".join([f"car.{key} = ${key}" for key in kwargs])
        query = f"MATCH (car:Car) WHERE ID(car) = $car_id SET {set_clause} RETURN car"
        kwargs["car_id"] = car_id
        return self.execute_query(query, kwargs)

    def delete_car(self, car_id):
        query = "MATCH (car:Car) WHERE ID(car) = $car_id DELETE car"
        return self.execute_query(query, {"car_id": car_id})

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return result.single() if result else None
