from db import driver
from db_utils import DatabaseSession  # Importing our DatabaseSession context managerpython -m api

class CarModel:
    def __init__(self, driver):
        self.driver = driver
        # Initialize other attributes as needed


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
        CREATE (car1:Car {make: 'Toyota', model: 'Corolla', year: 2020, location: 'Location A', status: 'available'})
        WITH car1
        CREATE (car2:Car {make: 'Honda', model: 'Civic', year: 2021, location: 'Location B', status: 'available'})
        WITH car1, car2
        CREATE (car3:Car {make: 'Ford', model: 'Focus', year: 2019, location: 'Location C', status: 'available'})
        RETURN id(car1) AS car1_id, id(car2) AS car2_id, id(car3) AS car3_id
        """
        return self.execute_query(query)

    def post_car(self, make, model, year, location, status, dry_run=False):
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

    def execute_query(self, query, parameters=None, dry_run=False):
        with DatabaseSession(self.driver, dry_run=dry_run) as session:
            result = session.run(query, parameters)  # Run the query and store the result
            return list(result)  # Convert the result to a list for easy iteration
        # Convert the result to a JSON-serializable format
            if result:
            # If there is a single result, convert it to a dictionary
                if isinstance(result.single(), dict):
                    return result.single()
                else:
                    return {key: value for record in result for key, value in record.items()}
            return None

        
        
