import unittest
from Engines.Sternman import Sternman
from Engines.Capulet import Capulet
from Engines.Willoughby import Willoughby


class TestEngine(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.last_service_mileage = 0
        self.current_mileage = 0
        self.capulet_engine = Capulet(lastServiceMileage=self.last_service_mileage, currentMileage=self.current_mileage)
        self.sternman_engine = Sternman(warningLightOn=False)
        self.willoughby_engine = Willoughby(lastServiceMileage=self.last_service_mileage,
                                            currentMileage=self.current_mileage)

    def test_capulet_needs_service(self):
        print('test_capulet_needs_service')
        self.assertFalse(self.capulet_engine.needs_service())

        self.capulet_engine.current_mileage = 30001

        self.assertTrue(self.capulet_engine.needs_service())

    def test_sternman_needs_service(self):
        print('test_sternman_needs_service')
        self.assertFalse(self.sternman_engine.needs_service())

        self.sternman_engine.warning_light_on = True

        self.assertTrue(self.sternman_engine.needs_service())

    def test_willoughby_needs_service(self):
        print('test_willoughby_needs_service')
        self.assertFalse(self.willoughby_engine.needs_service())

        self.willoughby_engine.current_mileage = 600001

        self.assertTrue(self.willoughby_engine.needs_service())
