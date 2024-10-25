from flask import Blueprint, request, jsonify
from models.car_model import CarModel
from config import driver

# Initialize Blueprint for rental routes
rental_bp = Blueprint('rental_bp', __name__)

# Initialize the CarModel with the Neo4j driver for rental operations
car_model = CarModel(driver)

@rental_bp.route('/order-car', methods=['POST'])
def order_car():
    data = request.json
    result = car_model.order_car(data['customer_id'], data['car_id'])
    return jsonify(result=result)

@rental_bp.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    data = request.json
    result = car_model.cancel_order_car(data['customer_id'], data['car_id'])
    return jsonify(result=result)

@rental_bp.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.json
    result = car_model.rent_car(data['customer_id'], data['car_id'])
    return jsonify(result=result)

@rental_bp.route('/return-car', methods=['POST'])
def return_car():
    data = request.json
    result = car_model.return_car(data['customer_id'], data['car_id'], data['status'])
    return jsonify(result=result)
