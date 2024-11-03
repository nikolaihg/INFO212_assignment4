from flask import Blueprint, request, jsonify
from models.car_model import CarModel
from db import driver

# Initialize Blueprint for car routes
car_bp = Blueprint('car_bp', __name__)

@car_bp.route('/cars', methods=['POST'])
def post_car():
    data = request.get_json()  # Get JSON data from the request
    if not all(key in data for key in ('make', 'model', 'year', 'location', 'status')):
        return jsonify({"error": "Missing required fields"}), 400
    
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    
    car_model = CarModel(driver)
    
    # Create the query to create the car node
    query = f"""
    CREATE (car:Car {{
        make: '{data['make']}', 
        model: '{data['model']}', 
        year: '{data['year']}', 
        location: '{data['location']}', 
        status: '{data['status']}'
    }})
    RETURN car
    """
    
    # Execute the query
    result = car_model.execute_query(query)
    
    # Assuming result contains the created car node
    created_car_node = result[0]['car']  # Adjust based on your actual result structure
    
    # Convert the node to a dictionary
    created_car = {
        'id': created_car_node.id,
        'make': created_car_node['make'],
        'model': created_car_node['model'],
        'year': created_car_node['year'],
        'location': created_car_node['location'],
        'status': created_car_node['status']
    }
    
    return jsonify(car=created_car), 201 if not dry_run else 200

@car_bp.route('/cars', methods=['GET'])
def list_cars():
    car_model = CarModel(driver)
    query = "MATCH (car:Car) RETURN car"
    cars = car_model.execute_query(query)

    # Construct a list of car dictionaries with IDs
    car_list = []
    for record in cars:
        car_data = record["car"]
        car_id = car_data.id  # Accessing the ID directly from the node
        car_list.append({"id": car_id, **car_data})  # Include the ID with the car data

    return jsonify(cars=car_list)


@car_bp.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    print(f"Requested car ID: {car_id}")  # Log the incoming request
    car_model = CarModel(driver)
    car = car_model.read_car(car_id)
    
    if car:
        print(f"Retrieved car: {car}")  # Log the retrieved car
        return jsonify(car=car), 200
    else:
        print(f"No car found with ID: {car_id}")  # Log if no car found
        return jsonify(error="Car not found"), 404


@car_bp.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.json
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    car_model = CarModel(driver)
    updated_car = car_model.update_car(car_id, dry_run=dry_run, **data)
    return jsonify(car=updated_car), 200 if not dry_run else 200


@car_bp.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    car_model = CarModel(driver)
    car_model.delete_car(car_id, dry_run=dry_run)
    return jsonify(message="Car deleted" if not dry_run else "Dry run: Car deletion rolled back"), 204 if not dry_run else 200

