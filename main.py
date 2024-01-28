import pymysql
from config_sql import host, user, password, db_name
from passenger_car import PassengerCar
from insert_user import insert_user
from insert_transport import insert_transport
from create_drop_table import create_tables, drop_tables

connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    db=db_name,
    cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:                                 # проверка существования таблиц
    name_table_query = f"SHOW TABLES LIKE '%'"
    flag = cursor.execute(name_table_query)

if not flag:                                                        # создать таблицы (если их нет в БД)
    create_tables(connection, 'users', 'transport')

email = 'Q'                                                         # вход/проверка пользователя
if email == 'Q':
    email = input("Введите свою электронную почту\n")
    with connection.cursor() as cursor:
        check_email = f"SELECT id, name FROM users WHERE email = '{email}'"
        cursor.execute(check_email)
        res = cursor.fetchone()
    if res:
        user_id, user_name = res.values()
    if not res:
        print('Такого пользователя нет. Пройдите регистрацию')     # регистрация нового пользователя
        user_name = input('Your name\n')
        password = input('Password\n')
        email = input('Email\n')
        insert_user(connection, user_name, password, email)
        with connection.cursor() as cursor:
            user_id_query = f"SELECT id FROM users WHERE email = '{email}'"
            cursor.execute(user_id_query)
            user_id = cursor.fetchone()['id']
print(f"Добро пожаловать {user_name}")


with connection.cursor() as cursor:
    obj_query = f"SELECT car_obj FROM transport WHERE autor_id = '{user_id}'"
    cursor.execute(obj_query)
    user_objects_list = cursor.fetchall()

if not user_objects_list:
    print('У Вас пока нет автомобилей в парке. Давай создадим!')
    car_type = input('Выберите категорию авто (В / С) \n')




order = ''
while order != 'exit':
    print(order)
    order = input("Введите команду\n")



















# p_car = PassengerCar('Ai 95', 50, 11, 'Green')
# print(p_car)
# p_car.go(450)
# print()
# p_car.go(100)
# #p_car.beep()
# print()
# p_car.fill_car('Ai 95', 10.5)
# p_car.go(100)

# if flag:                                                 #удалить таблицы
#     drop_tables(connection, 'users', 'transport')

connection.close()
