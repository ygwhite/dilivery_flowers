import psycopg2
from configBD import host, db_name, password, user


class RegData:

    def __init__(self, email):
        self.connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user_data,
            password=password
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name FROM users WHERE (email = %s)", (email,)
                )
                self.id_user = cursor.fetchall()
                cursor.execute(
                    """INSERT INTO cart (user_id) VALUES (%s);""",
                    (self.id_user[0][0],)
                )
                self.connection.commit()
                # self.list_flower = cursor.fetchall()



        finally:
            if self.connection:
                self.connection.close()
