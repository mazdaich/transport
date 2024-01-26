def insert_user(connection, user_name, user_password, user_email):
    with connection.cursor() as cursor:
        insert_query = f"""INSERT INTO `users` (name, password, email) 
                           VALUES ('{user_name}', '{user_password}', '{user_email}');"""
        cursor.execute(insert_query)
        connection.commit()







if __name__ == '__main__':
    insert_user('Timyr', 'qwerty', 'Timyr@gmail.com')
