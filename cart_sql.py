import psycopg2
from configBD import host, db_name, password, user


class CartFlowerUser:

    def __init__(self, username):
        self.connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password,
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "select f.flower, sum(f.price), sum(cf.quantity) from users u left join cart on cart.user_id = u.id left join cart_flower cf on cf.cart_id = cart.id left join flowers f on f.id = cf.flower_id where (username = %s) group by u.username, f.flower;",
                    (username,)
                )
                self.cart_user_flower = cursor.fetchall()



                self.connection.commit()
                # self.list_flower = cursor.fetchall()



        finally:
            if self.connection:
                self.connection.close()


# class DeleteFlower:
#
#     def __init__(self, username):
#         self.connection = psycopg2.connect(
#             host=host,
#             database=db_name,
#             user=user,
#             password=password,
#         )
#         try:
#             with self.connection.cursor() as cursor:
#                 cursor.execute(
#                     "DELETE FROM cart_user WHERE id = 123;",
#                     (username,)
#                 )
#                 self.cart_user_flower = cursor.fetchall()
#                 self.connection.commit()
#                 # self.list_flower = cursor.fetchall()
#
#
#
#         finally:
#             if self.connection:
#                 self.connection.close()

a = CartFlowerUser('dasfwe')
print(a.cart_user_flower)