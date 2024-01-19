from all_transport import Transport
from playsound import playsound


class PassengerCar(Transport):
    def beep(self):
        playsound('C:\\P.Projects\\Transport\\sound_for_python\\p_car_sound.mp3')



def test_car():
    p_car = PassengerCar('Ai 95', 50, 10, 'Green')
    print(p_car)
    p_car.go(100)
    p_car.beep()
    p_car.fill_car('Ai 9', 3)


if __name__ == '__main__':
    test_car()
