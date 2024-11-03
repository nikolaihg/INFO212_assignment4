from flask import Flask, request, jsonify
from database import Config, db_session, close_db
from controllers.car_controller import car_blueprint
from controllers.customer_controller import customer_blueprint
from controllers.employee_controller import employee_blueprint

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(car_blueprint, url_prefix='/cars')
app.register_blueprint(customer_blueprint, url_prefix='/customers')
app.register_blueprint(employee_blueprint, url_prefix='/employees')
# app.register_blueprint(order_blueprint, url_prefix='/orders')

@app.route('/')
def index():
    return "<h1>API is running</h1>"

# Ensure the driver closes when the app stops
@app.teardown_appcontext
def close_driver(exception=None):
    close_db()

# Run the app
if __name__ == "__main__":
     app.run(debug=app.config['DEBUG'])
