from Batteries.IBattery import IBattery
from helpful_scripts import SPINDLER_SERVICE_THRESHOLD


class SpindlerBattery(IBattery):

    def __init__(self, lastServiceDate, currentDate):
        self.last_service_date = lastServiceDate
        self.current_date = currentDate

    def needs_service(self) -> bool:
        return self.last_service_date.replace(
            year=self.last_service_date.year + SPINDLER_SERVICE_THRESHOLD) < self.current_date
