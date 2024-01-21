import pymysql
from config_sql import host, user, password, db_name


def insert_user(user_name, user_password, user_email):
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `users` (name, password, email)" \
                       f"VALUES ('{user_name}', '{user_password}', '{user_email}');"
        cursor.execute(insert_query)
        connection.commit()

    connection.close()


if __name__ == '__main__':
    insert_user('Marina', 'qwerty', 'Marina@gmail.com')
