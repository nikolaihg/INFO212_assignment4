from flask import Blueprint, request, jsonify
from models.employee_model import EmployeeModel  # Import the Employee model
from config import driver

# Initialize Blueprint for employee routes
employee_bp = Blueprint('employee_bp', __name__)

# Initialize the EmployeeModel with the Neo4j driver
employee_model = EmployeeModel(driver)

@employee_bp.route('/', methods=['POST'])
def create_employee():
    data = request.json
    employee = employee_model.create_employee(data['name'], data['address'], data['branch'])
    return jsonify(employee=employee), 201

@employee_bp.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = employee_model.read_employee(employee_id)
    return jsonify(employee=employee)

@employee_bp.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    updated_employee = employee_model.update_employee(employee_id, **data)
    return jsonify(employee=updated_employee)

@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee_model.delete_employee(employee_id)
    return jsonify(message="Employee deleted"), 204
