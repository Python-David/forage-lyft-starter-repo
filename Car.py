from abc import ABC, abstractmethod
from Battery import SpindlerBattery, NubinBattery
from Engine import Capulet, Willoughby, Sternman


class IServiceable(ABC):
    """Cars are accessed through the Serviceable interface"""

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(IServiceable):
    def __init__(self):
        self.engine = None
        self.battery = None

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False


class CarFactory:
    """Factory that creates cars"""

    def __init__(self):
        self.car = Car()

    def create_calliope(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        self.car.battery = SpindlerBattery(lastServiceDate, currentDate)
        self.car.engine = Capulet(lastServiceMileage, currentMileage)
        return self.car

    def create_glissade(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        self.car.battery = SpindlerBattery(lastServiceDate, currentDate)
        self.car.engine = Willoughby(lastServiceMileage, currentMileage)
        return self.car

    def create_palindrome(self, currentDate, lastServiceDate, warningLightOn):
        self.car.battery = SpindlerBattery(lastServiceDate, currentDate)
        self.car.engine = Sternman(warningLightOn)
        return self.car

    def create_rorschach(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        self.car.battery = NubinBattery(lastServiceDate, currentDate)
        self.car.engine = Willoughby(lastServiceMileage, currentMileage)
        return self.car

    def create_thovex(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        self.car.battery = NubinBattery(lastServiceDate, currentDate)
        self.car.engine = Capulet(lastServiceMileage, currentMileage)
        return self.car
