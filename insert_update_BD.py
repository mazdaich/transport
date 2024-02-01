import pymysql
from config_sql import host, user, password, db_name
import json


def insert_transport(connection, u_email, car_number):
    with connection.cursor() as cursor:
        select_query = f"SELECT id FROM users WHERE email = '{u_email}'"
        cursor.execute(select_query)
        u_id = (cursor.fetchone()['id'])

        insert_query = f"INSERT INTO transport (car_number, autor_id) VALUES ('{car_number}', '{u_id}');"
        cursor.execute(insert_query)
        connection.commit()


def update_transport(connection, car_obj, u_id, car_number):
    with connection.cursor() as cursor:
        insert_query = f"UPDATE transport SET car_obj = '{car_obj}' WHERE autor_id = '{u_id}' AND car_number = '{car_number}';"
        cursor.execute(insert_query)
        connection.commit()


def insert_user(connection, user_name, user_password, user_email):
    with connection.cursor() as cursor:
        insert_query = f"""INSERT INTO `users` (name, password, email) 
                           VALUES ('{user_name}', '{user_password}', '{user_email}');"""
        cursor.execute(insert_query)
        connection.commit()


if __name__ == '__main__':
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor)

    args = {'type_fuel': 'Ai 95', 'size_fuel_tank': 70, 'consumption_fuel': 0.11, 'color': 'white', 'x': 14, 'y': 0,
            'mileage': 450, 'fuel_in_tank': 12, 'flag': True}
    json_data = json.dumps(args)
    car_number = '002'

    #insert_transport(connection, 'Timyr@mail.ru', car_number)
    update_transport(connection, json_data, 1, car_number)

    connection.close()
