from flask import jsonify
from db import _get_connection, node_to_json
from models.status import Status

class Car:
    id=0
    def __init__ (self, make, model, year, location):
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        self.status = Status.available
        
    def __str__(self):
        return f"Car ({self.make}, {self.model}, {self.year}, {self.location}, {self.status.name})"

def get_all_cars():
    with _get_connection().session() as session:
        cars = session.run("MATCH (c:Car) RETURN c;") # get id: # MATCH (c:Car) RETURN id(c), c
        nodes_json = [node_to_json(record["c"]) for record in cars]
        print(nodes_json)
        return nodes_json


def create_car(make, model, year, location, status =Status.available.name):
    try:
        records, _, _ = _get_connection().execute_query(
            "CREATE (c:Car {make:$make, model:$model, year:$year, location:$location, status:$status}) RETURN c;",
            make=make,
            model=model,
            year=year,
            location=location,
            status=status
        )
        json_nodes = [node_to_json(rec["c"]) for rec in records]
        print(json_nodes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    if records is not None:
        return jsonify(json_nodes), 200
    else:
        return jsonify({'error': 'No data returned from query'}), 500


def delete_car(id):
    try:
        _get_connection().execute_query(
            "MATCH (c:Car) "
            f"WHERE ID(c) = {id} "
            "DETACH DELETE c;"
        )
    except Exception as e:
        return e
    return "Car is deleted."


def update_car(id, make, model, year, location, status):
    def check_input(new_val, current_val):
        if new_val != "":
            return new_val
        else:
            return  current_val
    try:
        nodes, _ ,_  = _get_connection().execute_query(
            "MATCH (c:Car) "
            f"WHERE ID(c) = {id} "
            "RETURN c; "
        )
        car = node_to_json(nodes[0]["c"])
    except Exception as e:
        return e
    print(car)
    if len(car) > 0:
        make = check_input(make, car["make"])
        model = check_input(model, car["model"])
        year = check_input(year, car["year"])
        location = check_input(location, car["location"])
        status = check_input(status, car["status"])
        result, _, _ = _get_connection().execute_query(
            "MATCH (c:Car) "
            f"WHERE ID(c) = {id} "
            f"SET c.make='{make}', c.model='{model}', c.year='{year}', c.location='{location}', c.status='{status}' "
            "RETURN c "
            )
        print(result)
        newnodes = [node_to_json(record["c"]) for record in result]
        return newnodes
