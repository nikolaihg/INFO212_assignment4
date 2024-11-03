from flask import Blueprint, request, jsonify
from models.employee_model import EmployeeModel
from db import driver

# Initialize Blueprint for employee routes
employee_bp = Blueprint('employee_bp', __name__)

# Route to create a new employee
@employee_bp.route('/', methods=['POST'])
def create_employee():
    data = request.json
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    employee_model = EmployeeModel(driver)
    employee = employee_model.create_employee(data['name'], data['address'], data['branch'], dry_run=dry_run)
    return jsonify(employee=employee), 201 if not dry_run else 200

# Route to retrieve an employee by ID
@employee_bp.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee_model = EmployeeModel(driver)
    employee = employee_model.read_employee(employee_id)
    return jsonify(employee=employee)

# Route to update an employee's information
@employee_bp.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    employee_model = EmployeeModel(driver)
    updated_employee = employee_model.update_employee(employee_id, dry_run=dry_run, **data)
    return jsonify(employee=updated_employee), 200 if not dry_run else 200

# Route to delete an employee by ID
@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    dry_run = request.args.get('dry_run', 'true').lower() == 'true'  # Defaults to dry run
    employee_model = EmployeeModel(driver)
<<<<<<< HEAD
    result = employee_model.delete_employee(employee_id)
    return jsonify(result=result)
=======
    result = employee_model.delete_employee(employee_id, dry_run=dry_run)
    return jsonify(message="Employee deleted" if not dry_run else "Dry run: Employee deletion rolled back"), 204 if not dry_run else 200
>>>>>>> espen
