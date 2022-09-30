from Tires.ITires import ITires
from helpful_scripts import OCTOPRIME_TIRE_THRESHOLD


class Octoprime(ITires):

    def __init__(self, tireWearArray: list[float]):
        self.tire_wear_array = tireWearArray

    def needs_service(self):
        return sum(self.tire_wear_array) > OCTOPRIME_TIRE_THRESHOLD
