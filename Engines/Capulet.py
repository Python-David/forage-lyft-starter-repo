from Engines.IEngine import IEngine
from helpful_scripts import CAPULET_THRESHOLD_MILEAGE


class Capulet(IEngine):

    def __init__(self, lastServiceMileage, currentMileage):
        self.last_service_mileage = lastServiceMileage
        self.current_mileage = currentMileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > CAPULET_THRESHOLD_MILEAGE
