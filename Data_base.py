import psycopg2
from configBD import host, db_name, password, user
from sql_request import sql_request_add_flower, sql_request_name_flower

output = True


class DataOutput:

    def __init__(self, sql_request):
        self.connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    sql_request
                )
                self.connection.commit()
                self.list_flower = cursor.fetchall()



        finally:
            if self.connection:
                self.connection.close()


a = DataOutput(sql_request_name_flower)

# class AddFlowerToCart(DataOutput):
#     def __init__(self, sql_request, cart_id, flower_id, quantity):
#         super().__init__()
# d = DataOutput(sql_request_list_flower)
# for i in d.flower_list:
#     print(list(d.flower_list))

for i in range(len(a.list_flower)):
    print(a.list_flower[i][i])