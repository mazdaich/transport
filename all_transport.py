from dataclasses import dataclass


@dataclass
class Transport:
    type_fuel: str
    size_fuel_tank: int
    consumption_fuel: int
    wheels: int
    color: str

    def __post_init__(self):
        self.fuel_in_tank = self.size_fuel_tank

    def check_fuel(self, distance):
        return (self.fuel_in_tank - self.consumption_fuel * distance) >= 0

    def go(self, distance):
        if self.check_fuel(distance):
            self.fuel_in_tank = self.consumption_fuel * distance
            print(f'Едем {distance} км. Израсходовали {self.consumption_fuel * distance} литров.\n'f'В баке осталось {self.fuel_in_tank} литров')




if __name__ == '__main__':
    t = Transport('B', 'red')
    print(t)
