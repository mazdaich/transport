from all_transport import Transport
from playsound import playsound


class PassengerCar(Transport):
    def beep(self):
        playsound('C:\\P.Projects\\Transport\\sound_for_python\\p_car_sound.mp3')


if __name__ == '__main__':
    car = PassengerCar('Ai 95', 50, 11, 'white')
    print(car.__dict__)
    car.go(150)
    print(car.__dict__)
    car.go(150)
    print(car.__dict__)

    args = {'type_fuel': 'Ai 95', 'size_fuel_tank': 50, 'consumption_fuel': 0.11, 'color': 'white', 'x': 150, 'y': 0, 'mileage': 150, 'fuel_in_tank': 33.5, 'flag': True}
    car2 = PassengerCar(**args)
    print(car2.__dict__)