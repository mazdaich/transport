from dataclasses import dataclass
from abc import ABC, abstractmethod
from playsound import playsound
from Excep import LowFuel, FuelType
from random import randint


@dataclass
class Transport(ABC):
    type_fuel: str
    size_fuel_tank: int
    consumption_fuel: int
    color: str
    x: int = 0
    y: int = 0
    mileage: int = 0
    fuel_in_tank: int = 0
    flag: bool = False

    def __post_init__(self):
        if not self.flag:
            self.fuel_in_tank = self.size_fuel_tank
            self.consumption_fuel /= 100
        self.flag = True

    @abstractmethod
    def beep(self):
        pass

    def go(self, distance):
        try:
            LowFuel.check_fuel(self, distance)
            playsound('C:\\P.Projects\\Transport\\sound_for_python\\starting-p_car.mp3')  #звук должен быть изменяем КАК СДЕЛАТЬ?
            self.fuel_in_tank -= self.consumption_fuel * distance
            self.x += distance
            self.mileage += distance
            print(f'Едем {distance} км. Израсходовали {self.consumption_fuel * distance} л.\n'
                  f''f'В баке осталось {self.fuel_in_tank} л.')
        except LowFuel as e:
            print(e)

    def fill_car(self, type_fuel, quantity='full'):
        try:
            FuelType.check_type_fuel(self, type_fuel)
            res = self.size_fuel_tank - self.fuel_in_tank
            if quantity == 'full':
                self.fuel_in_tank += res
                print(f'Заправили до полного {res} л. В баке {self.fuel_in_tank} л.')
            else:
                if not isinstance(quantity, int | float):
                        raise TypeError('ОШИБОЧКА. Количество бензина должно быть указанно цифрами')
                all_fuel = quantity + self.fuel_in_tank
                if all_fuel <= self.size_fuel_tank:
                    self.fuel_in_tank += quantity
                    print(f'Заправили {quantity} л. В баке {self.fuel_in_tank} л.')
                elif all_fuel > self.size_fuel_tank:
                    self.fuel_in_tank += res
                    print(f'Заправили {res} л. В баке {self.fuel_in_tank} л.\n'
                          f'Возвращено {quantity - res}')
        except FuelType as e:
            print(e)
        except TypeError as e:
            print(e)


def create_car_num(connection):
    with connection.cursor() as cursor:
        num_query = f"SELECT car_number FROM transport"
        cursor.execute(num_query)
        num_list = [i['car_number'] for i in cursor.fetchall()]
    num = ''
    for _ in range(3):
        num += str(randint(0, 9))
    if num not in num_list:
        return num
    else:
        create_car_num(connection)



if __name__ == '__main__':
    pass
