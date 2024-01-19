from dataclasses import dataclass
from abc import ABC, abstractmethod
from playsound import playsound
from Excep import LowFuel, FuelType


@dataclass
class Transport(ABC):
    type_fuel: str
    size_fuel_tank: int
    consumption_fuel: int
    color: str

    def __post_init__(self):
        self.fuel_in_tank = self.size_fuel_tank
        self.consumption_fuel /= 100

    @abstractmethod
    def beep(self):
        pass

    def go(self, distance):
        try:
            LowFuel.check_fuel(self, distance)
            #playsound('C:\\P.Projects\\Transport\\sound_for_python\\starting-p_car.mp3')  #звук должен быть изменяем КАК СДЕЛАТЬ?
            self.fuel_in_tank -= self.consumption_fuel * distance
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


if __name__ == '__main__':
    pass
