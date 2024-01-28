def insert_transport(connection, u_id, car_obj):
    # with connection.cursor() as cursor:
    #     select_query = f"SELECT id FROM users WHERE name = '{u_id}'"
    #     cursor.execute(select_query)
    #     u_id = (cursor.fetchone()['id'])

    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `transport` (car_obj, autor_id) VALUES ('{car_obj}', '{u_id}');"
        cursor.execute(insert_query)
        connection.commit()





if __name__ == '__main__':
    insert_transport('Timyr', 'Test_1')
