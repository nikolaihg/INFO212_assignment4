from flask import Blueprint, request, jsonify
from models.car_model import CarModel
from db import driver

# Initialize Blueprint for car routes
car_bp = Blueprint('car_bp', __name__)

# Initialize CarModel with driver in each route function
@car_bp.route('/', methods=['POST'])
def create_car():
    data = request.json
    car_model = CarModel(driver)  # Pass driver here
    car = car_model.create_car(data['id'], data['make'], data['model'], data['year'], data['location'], data['status'], availability)
    return jsonify(car=car), 201

@car_bp.route('/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car_model = CarModel(driver)
    car = car_model.read_car(car_id)
    return jsonify(car=car)

# @car_bp.route('/', methods=['POST'])
# def create_car():
#     data = request.json
#     car = car_model.create_car(data['make'], data['model'], data['year'], data['location'], data['status'])
#     return jsonify(car=car), 201
# 
# @car_bp.route('/<int:car_id>', methods=['GET'])
# def get_car(car_id):
#     car = car_model.read_car(car_id)
#     return jsonify(car=car)
# 
# @car_bp.route('/<int:car_id>', methods=['PUT'])
# def update_car(car_id):
#     data = request.json
#     updated_car = car_model.update_car(car_id, **data)
#     return jsonify(car=updated_car)
# 
# @car_bp.route('/<int:car_id>', methods=['DELETE'])
# def delete_car(car_id):
#     car_model.delete_car(car_id)
#     return jsonify(message="Car deleted"), 204
