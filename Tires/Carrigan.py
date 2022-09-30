from Tires.ITires import ITires
from helpful_scripts import CARRIGAN_TIRE_THRESHOLD


class Carrigan(ITires):

    def __init__(self, tireWearArray: list[float]):
        self.tire_wear_array = tireWearArray

    def needs_service(self):
        for i in self.tire_wear_array:
            if i >= CARRIGAN_TIRE_THRESHOLD:
                return True
        return False
