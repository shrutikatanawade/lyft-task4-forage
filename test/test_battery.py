import unittest
from engine.model.battery import Spindler

class TestBattery(unittest.TestCase):

    def test_spindler_service_interval(self):
        spindler_battery = Spindler()
        # Verify that the service interval for Spindler batteries is now 3 years
        self.assertEqual(spindler_battery.service_interval, 3)
