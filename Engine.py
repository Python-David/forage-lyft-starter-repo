from abc import ABC, abstractmethod

CAPULET_THRESHOLD_MILEAGE = 30000
WILLOUGHBY_THRESHOLD_MILEAGE = 60000


class IEngine(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Capulet(IEngine):

    def __init__(self, lastServiceMileage, currentMileage):
        self.last_service_mileage = lastServiceMileage
        self.current_mileage = currentMileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > CAPULET_THRESHOLD_MILEAGE


class Willoughby(IEngine):

    def __init__(self, lastServiceMileage, currentMileage):
        self.last_service_mileage = lastServiceMileage
        self.current_mileage = currentMileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > WILLOUGHBY_THRESHOLD_MILEAGE


class Sternman(IEngine):

    def __init__(self, warningLightOn):
        self.warning_light_on = warningLightOn

    def needs_service(self):
        return self.warning_light_on
