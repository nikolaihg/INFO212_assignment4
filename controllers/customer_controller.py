from flask import Blueprint, request, jsonify, render_template, url_for
from models.customer import Customer

customer_blueprint = Blueprint('customer_blueprint', __name__)

@customer_blueprint.route('/create', methods=['POST'])
def generate_customer():
    if request.is_json:
        customer_info = request.get_json()
        customer = Customer.create_from_json(customer_info)
        return jsonify(customer), 201
    else:
        return jsonify({"Error": "Request must be JSON"}), 415

@customer_blueprint.route('/', methods=['GET'])
def retrieve_customers():
    customers = Customer.retrieve_all()
    return jsonify({"customers": customers}), 200  # TODO HTML

@customer_blueprint.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    if request.is_json:
        Customer.update(customer_id, request.get_json())
        return jsonify({"Success": "Customer updated"}), 200
    return jsonify({"Error": "Request must be JSON"}), 415

@customer_blueprint.route('/<int:customer_id>', methods=['DELETE'])
def remove_customer(customer_id):
    Customer.delete(customer_id)
    return jsonify({"Success": "Customer deleted"}), 200