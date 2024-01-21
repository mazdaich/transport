import pymysql
from config_sql import host, user, password, db_name


connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    db=db_name,
    cursorclass=pymysql.cursors.DictCursor
)

#insert data
with connection.cursor() as cursor:
    insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'Erte@gmail.com');"
    cursor.execute(insert_query)
    connection.commit()
#

#
# with connection.cursor() as cursor:
#     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Timyr', '159', 'Tim@gmail.com');"
#     cursor.execute(insert_query)
#     connection.commit()
#
# with connection.cursor() as cursor:
#     select_query = "SELECT * FROM transport"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# with connection.cursor() as cursor:
#     select_query = "SELECT id FROM users WHERE name = 'Anna'"
#     cursor.execute(select_query)
#     autor = (cursor.fetchone()['id'])
#     with connection.cursor() as cursor:
#         insert_query = f"INSERT INTO `transport` (car_obj, autor_id) VALUES ('Test_8', {autor});"
#         cursor.execute(insert_query)
#         connection.commit()
#
# with connection.cursor() as cursor:
#     select_query = "SELECT users.name, transport.car_obj FROM users INNER JOIN transport ON users.id = autor_id;"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)


connection.close()
