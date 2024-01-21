import pymysql
from config_sql import host, user, password, db_name

'''
Создается 2 таблицы в БД. 
связь - один ко многим
Один user имеет несколько созданных им объектов
'''

connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    db=db_name,
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    create_table_query = "CREATE TABLE `users`(" \
                         "id int AUTO_INCREMENT PRIMARY KEY," \
                         "name varchar(12) NOT NULL," \
                         "password varchar(8) NOT NULL," \
                         "email varchar(32) NOT NULL UNIQUE KEY);"
    cursor.execute(create_table_query)
    print("Table created successfully")

with connection.cursor() as cursor:
    create_table_query = "CREATE TABLE `transport`(" \
                         "id int AUTO_INCREMENT," \
                         "car_obj varchar(12)," \
                         "autor_id varchar(32)," \
                         "PRIMARY KEY (id));"
    cursor.execute(create_table_query)
    print("Table created successfully")

#drop table

# with connection.cursor() as cursor:
#     drop_table_query = "DROP TABLE `users`;"
#     cursor.execute(drop_table_query)
#
# with connection.cursor() as cursor:
#     drop_table_query = "DROP TABLE `transport`;"
#     cursor.execute(drop_table_query)


connection.close()
