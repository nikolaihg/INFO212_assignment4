import app
from flask import render_template, request
from db import *
from models.customer import Customer, getAllCustomers

@app.route("/customers_create", methods=["POST"])
def customers_create():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        address = request.form["address"]

        try:
            data = Customer.create_customer(name=name, age=age, address=address)
        except Exception as e:
            return str(e)
    
    return render_template("customers.html", data=data)

@app.route("/customers", methods=["GET"])
def customers_read():
    
    if request.method == "GET":
        data = getAllCustomers()
    return render_template("customers.html", customers=data)


@app.route("/customers_update", methods=["POST"])
def customers_update():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        age = request.form["age"]
        address = request.form["address"]

        try:
            data = Customer.update_customer(id=id, name=name, age=age, address=address)
        except Exception as e:
            return str(e)
    
    return render_template("customers.html", data=data)


@app.route("/customers_delete", methods=["POST"])
def customers_delete():
    if request.method == "POST":
        id = request.form["id"]

        try:
            data = Customer.delete_customer(id=id)
        except Exception as e:
            return str(e)
    
    return render_template("customers.html", data=data)

