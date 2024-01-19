from dataclasses import dataclass
from abc import ABC, abstractmethod
from playsound import playsound
from Excep import LowFuel


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


if __name__ == '__main__':
    pass
