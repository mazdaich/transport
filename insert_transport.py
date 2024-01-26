import pymysql
from config_sql import host, user, password, db_name


def insert_transport(user_name, car_obj):
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        select_query = f"SELECT id FROM users WHERE name = '{user_name}'"
        cursor.execute(select_query)
        u_id = (cursor.fetchone()['id'])

    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `transport` (car_obj, autor_id) VALUES ('{car_obj}', '{u_id}');"
        cursor.execute(insert_query)
        connection.commit()

    connection.close()


if __name__ == '__main__':
    insert_transport('Timyr', 'Test_1')
