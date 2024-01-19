
class LowFuel(Exception):
    @staticmethod
    def check_fuel(obg, distance):
        if (obg.fuel_in_tank - obg.consumption_fuel * distance) >= 0:
            return True
        raise LowFuel(
            f'Недостаточно топлива\n'
            f'Чтобы проехать {distance} км. нужно {obg.consumption_fuel * distance} л. топлива\n'
            f'Сейчас в баке {obg.fuel_in_tank} л.,'
            f" не хватает {format(obg.consumption_fuel * distance - obg.fuel_in_tank, '.2f')} л."
        )


class FuelType(Exception):
    @staticmethod
    def check_type_fuel(obg, type_f):
        if isinstance(type_f, str):
            if type_f == obg.type_fuel:
                return True
        raise FuelType(f'Этот транспорт можно заправлять только {obg.type_fuel}')
