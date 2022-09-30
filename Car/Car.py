from Serviceable import IServiceable


class Car(IServiceable):
    def __init__(self):
        self.engine = None
        self.battery = None

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
