from db import _get_connection, node_to_json
from models.status import Status

class Customer:
    def __init__ (self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def create_customer (name, age, address):
        customer = Customer(name,age,address)
        try:
            data = _get_connection().execute_query(
                "create (c:Customer {name: $name, age: $age, address: $address}) RETURN c",
                name = name,
                age = age,
                address = address
            )
        except Exception as e:
            print(e)
        return customer
    
    def update_customer (id, name='', age='', address=''):
        #customer = Customer(name,age,address)
        try:
            #VIKTIG! denne fungerer kun når man bruker "" rundt strenger i postman formet
            data = _get_connection().execute_query(
                f"MATCH (p:Customer) WHERE ID(p) = {id} SET p.name = {name}, p.age = {age}, p.address = {address} RETURN p",
            )
        except Exception as e:
            print(e)
        
        print(name, age, address, "has been updated")
        return "testmelding fra update_customer"

    def delete_customer (id):
        try:
            data = _get_connection().execute_query(
                f"MATCH (c:Customer) WHERE ID(c) = {id} DETACH DELETE c",
            )
        except Exception as e:
            print(e)
        return "customer user deleted"
    
    
def getAllCustomers():
    with _get_connection().session() as session:
        customers = session.run("MATCH (c:Customer) RETURN c;")
        nodes_json = [node_to_json(record["c"]) for record in customers]
        print (nodes_json)
        return nodes_json



    