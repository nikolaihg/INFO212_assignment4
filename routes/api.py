from flask import Blueprint, jsonify, request

api_blueprint = Blueprint('api', __name__)

# Example route
@api_blueprint.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "API is working"})
