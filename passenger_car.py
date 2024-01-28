from all_transport import Transport
from playsound import playsound


class PassengerCar(Transport):
    def beep(self):
        playsound('C:\\P.Projects\\Transport\\sound_for_python\\p_car_sound.mp3')

