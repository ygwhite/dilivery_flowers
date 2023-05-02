import psycopg2
from configBD import host, db_name, password, user


class add_flower_to_cart:

    def __init__(self, flower_id, cart_id, quantity):
        self.connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """insert into cart_flower (flower_id, cart_id, quantity) VALUES (%s, %s, %s)""",
                    (flower_id, cart_id, quantity),
                )
                cursor.execute(
                    "SELECT id FROM cart_flower WHERE (cart_id = %s)", (cart_id,)
                )
                self.id_cart_flower = cursor.fetchall()
                self.connection.commit()
                self.list_flower = cursor.fetchall()



        finally:
            if self.connection:
                self.connection.close()


a = add_flower_to_cart(1, 2, 1)
