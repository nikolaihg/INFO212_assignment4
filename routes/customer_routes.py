from flask import Blueprint, request, jsonify
from models.customer_model import CustomerModel
from db import driver

# Initialize Blueprint for customer routes
customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    customer_model = CustomerModel(driver)
    customer = customer_model.create_customer(data['name'], data['age'], data['address'], dry_run=dry_run)
    return jsonify(customer=customer), 201 if not dry_run else 200

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer_model = CustomerModel(driver)
    customer = customer_model.read_customer(customer_id)
    return jsonify(customer=customer)

@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.json
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    customer_model = CustomerModel(driver)
    updated_customer = customer_model.update_customer(customer_id, dry_run=dry_run, **data)
    return jsonify(customer=updated_customer), 200 if not dry_run else 200

<<<<<<< HEAD
# @customer_bp.route('/', methods=['POST'])
# def create_customer():
#     data = request.json
#     customer = customer_model.create_customer(data['name'], data['age'], data['address'])
#     return jsonify(customer=customer), 201
# 
# @customer_bp.route('/<int:customer_id>', methods=['GET'])
# def get_customer(customer_id):
#     customer = customer_model.read_customer(customer_id)
#     return jsonify(customer=customer)
# 
# @customer_bp.route('/<int:customer_id>', methods=['PUT'])
# def update_customer(customer_id):
#     data = request.json
#     updated_customer = customer_model.update_customer(customer_id, **data)
#     return jsonify(customer=updated_customer)
# 
# @customer_bp.route('/<int:customer_id>', methods=['DELETE'])
# def delete_customer(customer_id):
#     customer_model.delete_customer(customer_id)
#     return jsonify(message="Customer deleted"), 204
=======
@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    customer_model = CustomerModel(driver)
    customer_model.delete_customer(customer_id, dry_run=dry_run)
    return jsonify(message="Customer deleted" if not dry_run else "Dry run: Customer deletion rolled back"), 204 if not dry_run else 200
>>>>>>> espen
