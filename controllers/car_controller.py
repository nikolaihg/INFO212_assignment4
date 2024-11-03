import app
from flask import render_template, request
from db import *
from models.car import Car, create_car, update_car, delete_car, get_all_cars

@app.route("/cars_get", methods = ["GET"])
def cars_get():
    return get_all_cars()
    

@app.route("/cars_create", methods = ["POST"])
def cars_create():
    make = request.form["make"]
    model = request.form["model"]
    year = request.form["year"]
    location = request.form["location"]
    try:
        data = create_car(make=make, model=model, year=year, location=location)
        print(data)
    except Exception as e:
        return e
    return data

@app.route("/cars_update", methods = ["POST"])
def cars_update():
    car_id = request.form["car_id"]
    make = request.form["make"]
    model = request.form["model"]
    year = request.form["year"]
    location = request.form["location"]
    status = request.form["status"]
    data = update_car(car_id, make, model, year, location, status)
    return data

@app.route("/cars_delete", methods = ["POST"])
def cars_delete():
    car_id = request.form["car_id"]
    print("To delete: ", car_id)
    return delete_car(car_id)
