from flask import Flask, Blueprint
from routes.car_routes import car_bp
from routes.customer_routes import customer_bp
from routes.employee_routes import employee_bp
from routes.rental_routes import rental_bp

app = Flask(__name__)
app.register_blueprint(car_bp)
with app.app_context():
    print(app.url_map)
if __name__ == "__main__":
    app.run(debug=True)

# Create a main API blueprint to combine individual blueprints
api_bp = Blueprint('api', __name__)

# Register each blueprint with the main API blueprint
api_bp.register_blueprint(car_bp, url_prefix='/cars')
api_bp.register_blueprint(customer_bp, url_prefix='/customers')
api_bp.register_blueprint(employee_bp, url_prefix='/employees')
api_bp.register_blueprint(rental_bp, url_prefix='/rentals')