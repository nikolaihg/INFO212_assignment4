import app
from flask import render_template, request, redirect, url_for
from db import *
import datetime
from models.endpoint import Endpoint
from models.car import get_all_cars

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "GET":
        cars = get_all_cars()
    else:
        cars = []
    return render_template("Welcome.html"
                           , utc_dt = datetime.datetime.utcnow()
                           , cars = cars)


@app.route("/car_order", methods=["POST"])
def car_order():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        car_id = request.form["car_id"]

        try:
            data = Endpoint.order_car(customer_id=customer_id, car_id = car_id)
            
        except Exception as e:
            return str(e)
    
    return render_template("welcome.html", data=data)

@app.route("/cancel_car_order", methods=["POST"])
def cancel_car_order():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        car_id = request.form["car_id"]

        try:
            data = Endpoint.cancel_order_car(customer_id=customer_id, car_id = car_id)
            
        except Exception as e:
            return str(e)
    
    return render_template("welcome.html", data=data)

@app.route("/car_rent", methods=["POST"])
def car_rent():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        car_id = request.form["car_id"]

        try:
            data = Endpoint.rent_car(customer_id=customer_id, car_id = car_id)
            
        except Exception as e:
            return str(e)
    
    return render_template("welcome.html", data=data)


@app.route("/car_return", methods=["POST"])
def car_return():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        car_id = request.form["car_id"]
        car_status = request.form["car_status"]

        try:
            data = Endpoint.return_car(customer_id=customer_id, car_id = car_id, car_status=car_status)
            
        except Exception as e:
            return str(e)
    
    return render_template("welcome.html", data=data)