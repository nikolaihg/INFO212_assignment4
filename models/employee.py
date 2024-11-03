from db import _get_connection, node_to_json
from models.status import Status

class Employee:
    def __init__ (self, name, address, branch):
        self.name = name
        self.address = address
        self.branch = branch
    
    def create_employee (name, address, branch):
        employee = Employee(name, address, branch)
        try:
            data = _get_connection().execute_query(
                "CREATE (c:Employee {name: $name, address: $address, branch: $branch}) RETURN c",
                name = name,
                address = address,
                branch=branch
            )
        except Exception as e:
            print(e)
        return employee
    
    def update_employee (id, name='', address='', branch = ''):
        try:
            #VIKTIG! denne fungerer kun når man bruker "" rundt strenger i postman formet
            data = _get_connection().execute_query(
                f"MATCH (p:Employee) WHERE ID(p) = {id} SET p.name = {name}, p.address = {address}, p.branch = {branch} RETURN p",
            )
        except Exception as e:
            print(e)
    
    def delete_employee (id):
        try:
            data = _get_connection().execute_query(
                f"MATCH (c:Employee) WHERE ID(c) = {id} DETACH DELETE c",
            )
        except Exception as e:
            print(e)
        return "employee user deleted"

def getAllEmployees():
    with _get_connection().session() as session:
        employees = session.run("MATCH (c:Employee) RETURN c;")
        nodes_json = [node_to_json(record["c"]) for record in employees]
        print (nodes_json)
        return nodes_json