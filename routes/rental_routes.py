from flask import Blueprint, request, jsonify
from models.car_model import CarModel
from db import driver

# Initialize Blueprint for rental routes
rental_bp = Blueprint('rental_bp', __name__)

@rental_bp.route('/order-car', methods=['POST'])
def order_car():
    data = request.json
    make = data.get('make')
    model = data.get('model')
    year = data.get('year')
    location = data.get('location')
    status = data.get('status')

    if not all([make, model, year, location, status, data.get('customer_id'), data.get('car_id')]):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Initialize CarModel with the Neo4j driver for this request
    car_model = CarModel(driver)
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    result = car_model.order_car(data['customer_id'], data['car_id'], dry_run=dry_run)

    return jsonify(result=result), 200 if dry_run else 201

@rental_bp.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    data = request.json

    if not all([data.get('customer_id'), data.get('car_id')]):
        return jsonify({"error": "Missing required fields"}), 400

    # Initialize CarModel with the Neo4j driver for this request
    car_model = CarModel(driver)
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    result = car_model.cancel_order_car(data['customer_id'], data['car_id'], dry_run=dry_run)

    return jsonify(result=result), 200 if dry_run else 204

@rental_bp.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.json
    make = data.get('make')
    model = data.get('model')
    year = data.get('year')
    location = data.get('location')
    status = data.get('status')

    if not all([make, model, year, location, status, data.get('customer_id'), data.get('car_id')]):
        return jsonify({"error": "Missing required fields"}), 400

    # Initialize CarModel with the Neo4j driver for this request
    car_model = CarModel(driver)
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    result = car_model.rent_car(data['customer_id'], data['car_id'], dry_run=dry_run)

    return jsonify(result=result), 200 if dry_run else 201

@rental_bp.route('/return-car', methods=['POST'])
def return_car():
    data = request.json

    if not all([data.get('customer_id'), data.get('car_id'), data.get('status')]):
        return jsonify({"error": "Missing required fields"}), 400

    # Initialize CarModel with the Neo4j driver for this request
    car_model = CarModel(driver)
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    result = car_model.return_car(data['customer_id'], data['car_id'], data['status'], dry_run=dry_run)

    return jsonify(result=result), 200 if dry_run else 204