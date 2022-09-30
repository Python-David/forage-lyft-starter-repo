import unittest
from Batteries.Nubin import NubinBattery
from Batteries.Spindler import SpindlerBattery
from datetime import datetime


class TestBattery(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.today = datetime.today().date()
        self.nubin_last_service_date = self.today.replace(year=self.today.year - 3)
        self.spindler_last_service_date = self.today.replace(year=self.today.year - 2)
        self.nubin_battery = NubinBattery(currentDate=self.today, lastServiceDate=self.nubin_last_service_date)
        self.spindler_battery = SpindlerBattery(currentDate=self.today, lastServiceDate=self.spindler_last_service_date)

    def test_nubin_battery_needs_service(self):
        print('test_nubin_battery_needs_service')
        self.assertFalse(self.nubin_battery.needs_service())

        self.nubin_battery.last_service_date = self.today.replace(year=self.today.year - 5)

        self.assertTrue(self.nubin_battery.needs_service())

    def test_spindler_battery_needs_service(self):
        print('test_spindler_battery_needs_service')
        self.assertFalse(self.spindler_battery.needs_service())

        self.spindler_battery.last_service_date = self.today.replace(year=self.today.year - 5)

        self.assertTrue(self.spindler_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
