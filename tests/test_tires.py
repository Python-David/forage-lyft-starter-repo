import unittest
from Tires.Carrigan import Carrigan
from Tires.Octoprime import Octoprime


class TestTires(unittest.TestCase):
    def setUp(self):
        print('setUp')

        self.carrigan_tire_wear_array = [0.1, 0.2, 0.5, 0.95]
        self.octoprime_tire_wear_array = [0.5, 0.9, 0.7, 0.97]

        self.carrigan_tires = Carrigan(self.carrigan_tire_wear_array)
        self.octoprime_tires = Octoprime(self.octoprime_tire_wear_array)

    def test_carrigan_tires(self):
        print('test_carrigan_tires')
        self.assertTrue(self.carrigan_tires.needs_service())

        self.carrigan_tires.tire_wear_array = [0.1, 0.2, 0.5, 0.9]

        self.assertTrue(self.carrigan_tires.needs_service())

        self.carrigan_tires.tire_wear_array = [0.1, 0.2, 0.5, 0.7]

        self.assertFalse(self.carrigan_tires.needs_service())

    def test_octoprime_tires(self):
        print('test_octoprime_tires')
        self.assertTrue(self.octoprime_tires.needs_service())

        self.octoprime_tires.tire_wear_array = [0.5, 0.9, 0.7, 0.9]

        self.assertTrue(self.carrigan_tires.needs_service())

        self.octoprime_tires.tire_wear_array = [0.5, 0.9, 0.7, 0.6]

        self.assertFalse(self.octoprime_tires.needs_service())
