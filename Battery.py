from abc import ABC, abstractmethod

SPINDLER_SERVICE_THRESHOLD = 2
NUBIN_SERVICE_THRESHOLD = 4


class IBattery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class SpindlerBattery(IBattery):

    def __init__(self, lastServiceDate, currentDate):
        self.last_service_date = lastServiceDate
        self.current_date = currentDate

    def needs_service(self) -> bool:
        return self.last_service_date.replace(
            year=self.last_service_date.year + SPINDLER_SERVICE_THRESHOLD) < self.current_date


class NubinBattery(IBattery):

    def __init__(self, lastServiceDate, currentDate):
        self.last_service_date = lastServiceDate
        self.current_date = currentDate

    def needs_service(self) -> bool:
        return self.last_service_date.replace(
            year=self.last_service_date.year + NUBIN_SERVICE_THRESHOLD) < self.current_date
