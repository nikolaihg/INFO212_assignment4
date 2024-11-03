import app
from flask import render_template, request
from db import *
from models.employee import Employee, getAllEmployees

@app.route('/employees_create', methods = ["POST"])
def employees_create():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        branch = request.form["branch"]

        try:
            data = Employee.create_employee(name=name, address=address, branch=branch)
        except Exception as e:
            return str(e)
    
    elif request.method == "GET":
        data = None
    return render_template("employees.html", data=data)


@app.route('/employees', methods = ["GET"])
def employee_read():
    if request.method == "GET":
        data = getAllEmployees()
    return render_template("employees.html", employees=data)


@app.route('/employees_update', methods = ["POST"])
def employees_update():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        address = request.form["address"]
        branch = request.form["branch"]

        try:
            data = Employee.update_employee(id=id, name=name, address=address, branch=branch)
        except Exception as e:
            return str(e)
    
    return render_template("employees.html", data=data)


@app.route('/employees_delete', methods = ["POST"])
def employees_delete():
    if request.method == "POST":
        id = request.form["id"]

        try:
            data = Employee.delete_employee(id=id)
        except Exception as e:
            return str(e)
    
    return render_template("employees.html", data=data)


