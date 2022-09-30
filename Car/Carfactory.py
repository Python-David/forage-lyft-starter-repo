from Car.Car import Car
from Batteries.Nubin import NubinBattery
from Batteries.Spindler import SpindlerBattery
from Engines.Capulet import Capulet
from Engines.Willoughby import Willoughby
from Engines.Sternman import Sternman
from Tires.Carrigan import Carrigan
from Tires.Octoprime import Octoprime


class CarFactory:
    """Factory that creates cars"""

    def __init__(self):
        self.car = Car()

    def create_calliope(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireArray):
        self.car.battery = SpindlerBattery(lastServiceDate, currentDate)
        self.car.engine = Capulet(lastServiceMileage, currentMileage)
        self.car.tire_carrigan = Carrigan(tireArray)
        self.car.tire_octoprime = Octoprime(tireArray)
        return self.car

    def create_glissade(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireArray):
        self.car.battery = SpindlerBattery(lastServiceDate, currentDate)
        self.car.engine = Willoughby(lastServiceMileage, currentMileage)
        self.car.tire_carrigan = Carrigan(tireArray)
        self.car.tire_octoprime = Octoprime(tireArray)
        return self.car

    def create_palindrome(self, currentDate, lastServiceDate, warningLightOn, tireArray):
        self.car.battery = SpindlerBattery(lastServiceDate, currentDate)
        self.car.engine = Sternman(warningLightOn)
        self.car.tire_carrigan = Carrigan(tireArray)
        self.car.tire_octoprime = Octoprime(tireArray)
        return self.car

    def create_rorschach(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireArray):
        self.car.battery = NubinBattery(lastServiceDate, currentDate)
        self.car.engine = Willoughby(lastServiceMileage, currentMileage)
        self.car.tire_carrigan = Carrigan(tireArray)
        self.car.tire_octoprime = Octoprime(tireArray)
        return self.car

    def create_thovex(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireArray):
        self.car.battery = NubinBattery(lastServiceDate, currentDate)
        self.car.engine = Capulet(lastServiceMileage, currentMileage)
        self.car.tire_carrigan = Carrigan(tireArray)
        self.car.tire_octoprime = Octoprime(tireArray)
        return self.car
