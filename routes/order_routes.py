from flask import Blueprint, request, jsonify
from models.order_model import CustomerModel
from models.car_model import CarModel
from db import driver

order_bp = Blueprint("order_bp", __name__)

customer_model = CustomerModel(driver)
car_model = CarModel(driver)
@order_bp.route("/order-car", methods=["POST"])
def order_car():
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")

    if not customer_id or not car_id:
        return jsonify({"error" : "customer_id and car_id are required"}), 400

    result = car_model.order_car(customer_id, car_id)

    if result:
        return jsonify({"message" : "Car ordered successfully", "customer_id": customer_id, "car_id": car_id}), 201
    else:
        return jsonify({"error": "Failed to order car"}), 500

@order_bp.route("/cancle-order-car", methods=["POST"])
def cancel_car():
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")

    if not customer_id or not car_id:
        return jsonify({"error": "customer_id and car_id are not required"}), 400

    result = car_model.cancel_car(customer_id, car_id)

    if result:
        return jsonify({"message": "Car booking canceled successfully", "customer_id": customer_id, "car_id": car_id}), 200
    else:
        return jsonify({"error": "Failed to cancel car booking"}), 500

@order_bp.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")

    if not customer_id or not car_id:
        return jsonify({"error": "customer_id and car_id are required"}), 400

    result = car_model.rent_car(customer_id, car_id)

    if result:
        return jsonify({"message": "Car rented successfully", "customer_id": customer_id, "car_id": car_id}), 200
    else:
        return jsonify({"error": "Failed to rent car"}), 500


@order_bp.route('/return-car', methods=['POST'])
def return_car():
    data = request.get_json()
    customer_id = data.get("customer_id")
    car_id = data.get("car_id")
    car_status = data.get("status", "available")  # Default to 'available' if no status is provided

    if not customer_id or not car_id:
        return jsonify({"error": "customer_id and car_id are required"}), 400

    result = car_model.return_car(customer_id, car_id, car_status)

    if result:
        return jsonify({"message": "Car returned successfully", "customer_id": customer_id, "car_id": car_id, "status": car_status}), 200
    else:
        return jsonify({"error": "Failed to return car"}), 500