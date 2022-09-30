from Engines.IEngine import IEngine


class Sternman(IEngine):

    def __init__(self, warningLightOn):
        self.warning_light_on = warningLightOn

    def needs_service(self):
        return self.warning_light_on
