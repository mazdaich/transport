from dataclasses import dataclass
from all_transport import Transport


class PassengerCar(Transport):
    pass


if __name__ == '__main__':
    p_car = PassengerCar('Ai 95', 50, 1, 4, 'Green')
    print(p_car)
    p_car.go(10)
