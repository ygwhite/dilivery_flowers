import psycopg2
from configBD import host, db_name, password, user

sql_email_search = """SELECT * FROM users WHERE email = %s;"""
sql_request_add_flower = (
    """INSERT INTO users (name, username, email, password) 
                        VALUES (%s, %s, %s, %s);"""
)


class RegData:

    def __init__(self, name, username, email, password_user):
        self.connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user_data,
            password=password
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s);""",
                    (name, username, email, password_user),
                )
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


not_there_is_no_indentical_data = []


class SearchEmailAndUsername:

    def __init__(self, email, username):
        self.connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM users WHERE (email = %s) OR (username = %s)", (email, username)
                )
                self.connection.commit()
                email_and_username = cursor.fetchall()
                if email_and_username == not_there_is_no_indentical_data:
                    self.response = 'Accepted!'
                else:
                    self.response = 'Not accepted!'
                # self.list_flower = cursor.fetchall()



        finally:
            if self.connection:
                self.connection.close()


a = SearchEmailAndUsername('reekt@fck.com', 'Rusan')
print(a.response)
