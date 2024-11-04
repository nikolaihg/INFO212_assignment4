from flask import Blueprint, request, jsonify, render_template, url_for
from models.car import Car

car_blueprint = Blueprint('car_blueprint', __name__)

@car_blueprint.route('/create', methods=['POST'])
def generate_car():
    print("Received a POST request at /create")
    if request.is_json:
        car_data = request.get_json()
        car = Car.generate_from_json(car_data)
        return jsonify(car), 201  
    else:
        print("Data is not JSON")
        # TODO HTML Form version

@car_blueprint.route('/cars/', methods=['POST'])
def create_car():
    if request.is_json:
        car_data = request.get_json()
        try:
            car = Car.generate_from_json(car_data)
            return jsonify(car), 201
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Request must be JSON"}), 415

@car_blueprint.route('/', methods=['GET'])
def generate_cars():
    cars = Car.retrieve_all()
    
    # Improved check for JSON response format
    if request.accept_mimetypes['application/json'] >= request.accept_mimetypes['text/html']:
        return jsonify(cars)
    
    # Default to HTML if JSON is not explicitly requested
    return render_template('cars.html', cars=cars)

@car_blueprint.route('/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    if request.is_json:
        Car.update(car_id, request.get_json())
        return jsonify({"success": "Car updated successfully"}), 200
    return jsonify({"error": "Request must be JSON"}), 415

@car_blueprint.route('/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    Car.delete(car_id)
    return jsonify({"success": "Car deleted successfully"}), 200