from flask import Blueprint, request, jsonify
from models.customer_model import CustomerModel

# Initialize Blueprint for customer routes
customer_bp = Blueprint('customer_bp', __name__)

# Pass driver into each route function where it is needed
@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json
    customer_model = CustomerModel(driver)  # Use driver here
    customer = customer_model.create_customer(data['name'], data['age'], data['address'])
    return jsonify(customer=customer), 201

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer_model = CustomerModel(driver)
    customer = customer_model.read_customer(customer_id)
    return jsonify(customer=customer)


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
