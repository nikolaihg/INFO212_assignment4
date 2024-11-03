from db import _get_connection, node_to_json
from models.status import Status

class Endpoint:
    
    def order_car (customer_id, car_id):
        try:
            car = _get_connection().execute_query(
                f"MATCH (s:Car) WHERE ID(s) = {car_id} RETURN s.status",
            )

            cust = _get_connection().execute_query(
                f"""MATCH (s:Customer) 
                WHERE ID(s) = {customer_id} 
                OPTIONAL MATCH (s) -[r] -> () 
                RETURN COUNT(r)""",
                )
    
            customer_relation_count = cust[0][0][0]
            car_status = car[0][0][0]
                        
            if car_status == Status.available.name and customer_relation_count == 0:

                _get_connection().execute_query(
                f"""MATCH (s:Customer)
                WHERE ID(s) = {customer_id}
                MATCH (c:Car)
                WHERE ID(c) = {car_id}
                CREATE (s)-[r:BOOKS]->(c)
                SET c.status = "booked"
                RETURN s, r, c;
                """,
                )
            else: 
                return f"Order failed: car has status \"{car_status}\", and customer has {customer_relation_count} reservations."
        except Exception as e:
            return e
    

    def cancel_order_car (customer_id, car_id):
        try:
            car = _get_connection().execute_query(
                f"MATCH (s:Car) WHERE ID(s) = {car_id} RETURN s.status",
            )
            is_booked_by_customer = car_is_booked_by_customer(customer_id, car_id)
            car_status = car[0][0][0]
            print("success1")
            if car_status == "booked" and is_booked_by_customer:
                print("success2")
                

                _get_connection().execute_query(
                f"""MATCH (s:Customer)-[r:BOOKS] -> (c:Car)
                WHERE ID(s) = {customer_id} AND ID(c) = {car_id}
                DELETE r
                SET c.status = "available"
                RETURN s, c
                """,
                )
            else: 
                return f"Car has status: {car_status}, and customer already reserved car: {is_booked_by_customer}"
        except Exception as e:
            return e

    

    def rent_car (customer_id, car_id):
        is_booked_by_customer = car_is_booked_by_customer(customer_id, car_id)
        
        if is_booked_by_customer:
            _get_connection().execute_query(
                f"""MATCH (s:Customer)-[b:BOOKS] -> (c:Car)
                WHERE ID(s) = {customer_id} AND ID(c) = {car_id}
                DELETE b
                CREATE (s)-[r:RENTS]->(c)
                SET c.status = "rented"
                RETURN s, r, c;
                """,
                )
            
            return f"Car is now {Status.rented.name}"
            
        else: 
            print("Could not rent car. Car is not booked by this customer.")


    def return_car (customer_id, car_id, car_status):
        try:
            is_rented_by_customer = _get_connection().execute_query(
                f"""MATCH (a:Customer)
                WHERE ID(a) = {customer_id}
                WITH a
                MATCH (a)-[:RENTS]->(b)
                WHERE ID(b) = {car_id}
                RETURN COALESCE(COUNT(b), 0) > 0 AS hasBooksRelationship;
                """,
                )[0][0][0]
            
            if is_rented_by_customer:
                _get_connection().execute_query(
                f"""MATCH (s:Customer)-[b:RENTS] -> (c:Car)
                WHERE ID(s) = {customer_id} AND ID(c) = {car_id}
                DELETE b
                SET c.status = "{car_status}"
                RETURN s, c;
                """,
                )
            else: 
                return "Car is not rented by customer."
        except Exception as e:
            return e


def car_is_booked_by_customer(customer_id, car_id):

    try:
        is_booked_by_customer = _get_connection().execute_query(
            f"""MATCH (a:Customer)
            WHERE ID(a) = {customer_id}
            WITH a
            MATCH (a)-[:BOOKS]->(b)
            WHERE ID(b) = {car_id}
            RETURN COALESCE(COUNT(b), 0) > 0 AS hasBooksRelationship;
            """)[0][0][0]
        print("etteleraent")
        return is_booked_by_customer
    except Exception as e:
        return e

