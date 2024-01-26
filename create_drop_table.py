def create_tables(connection, name_table_1, name_table_2):
    """
    Создается 2 таблицы в БД.
    связь - один ко многим
    Один user имеет несколько созданных им объектов
    :param connection:
    :param name_table_1:
    :param name_table_2:
    :return: None
    """
    try:
        with connection.cursor() as cursor:
            create_table_query = f"""CREATE TABLE `{name_table_1}`(
                                    id int AUTO_INCREMENT PRIMARY KEY,
                                    name varchar(12) NOT NULL,
                                    password varchar(8) NOT NULL,
                                    email varchar(32) NOT NULL UNIQUE KEY
                                    );"""
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)

    try:
        with connection.cursor() as cursor:
            create_table_query = f"""CREATE TABLE `{name_table_2}`(
                                    id int AUTO_INCREMENT PRIMARY KEY,
                                    car_obj varchar(12),
                                    autor_id int,
                                    mileage int DEFAULT '0',
                                    FOREIGN KEY (autor_id)  REFERENCES users (id) ON DELETE CASCADE
                                    );"""
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)
    else:
        print("Tables created successfully")


def drop_tables(connection, name_table_1, name_table_2):
    """
    Уничтожение таблиц в БД
    :param connection:
    :param name_table_1:
    :param name_table_2:
    :return:
    """
    try:
        with connection.cursor() as cursor:
            drop_table_query = f"DROP TABLE `{name_table_2}`;"
            cursor.execute(drop_table_query)
    except Exception as e:
        print(e)

    try:
        with connection.cursor() as cursor:
            drop_table_query = f"DROP TABLE `{name_table_1}`;"
            cursor.execute(drop_table_query)
    except Exception as e:
        return e
    else:
        print(f'Tables deleted')
