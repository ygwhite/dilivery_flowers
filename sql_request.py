sql_request_name_flower = "SELECT flower, description, quantity, price FROM flowers;"
sql_request_add_flower = ("""INSERT INTO cart_flower (cart_id, flower_id, quantity) 
                    VALUES (%s, %s, %s);""",
                          (2, 1, 213))
sql_request_add_user = ("""INSERT INTO users (name, username, email, password) 
                    VALUES (%s, %s, %s);""",)
