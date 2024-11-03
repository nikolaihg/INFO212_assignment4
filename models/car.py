from database import db_session
from utils import node_to_dict

class Car:
    @staticmethod
    def generate_from_json(json_data):
        required_fields = ['make', 'model', 'year', 'location']
        if not all(field in json_data for field in required_fields):
            raise ValueError("Missing required fields in the input data")

        with db_session() as session:
            result = session.run(
                """
                CREATE (car:Car {make: $make, model: $model, year: $year, location: $location, status: 'available'})
                RETURN car
                """,
                make=json_data['make'],
                model=json_data['model'],
                year=json_data['year'],
                location=json_data['location']
            )
            node = result.single()[0] 
            return node_to_dict(node)  

    @staticmethod
    def retrieve_all():
        with db_session() as session:
            result = session.run("MATCH (car:Car) RETURN car, ID(car) as id") 
            cars = [dict(node_to_dict(record['car']), id=record['id']) for record in result]
            print("Retrieved cars:", cars)
            return cars

    @staticmethod
    def update(car_id, json_data):
        with db_session() as session:
            session.run(
                "MATCH (vehicle:Car) WHERE id(vehicle) = $car_id SET vehicle += $properties",
                car_id=car_id, properties=json_data
            )

    @staticmethod
    def delete(car_id):
        with db_session() as session:
            session.run("MATCH (vehicle:Car) WHERE id(vehicle) = $car_id DETACH DELETE vehicle", car_id=car_id)

    def to_dict(self):
        return dict(self)