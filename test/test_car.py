import unittest
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class TestCalliope(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 10000
        calliope = Calliope(last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 5000
        calliope = Calliope(last_service_mileage)
        self.assertFalse(calliope.needs_service())

class TestGlissade(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = '2023-01-01'
        glissade = Glissade(last_service_date)
        self.assertTrue(glissade.needs_service())

    def test_does_not_need_service(self):
        last_service_date = '2023-07-01'
        glissade = Glissade(last_service_date)
        self.assertFalse(glissade.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 8000
        warning_light_is_on = True
        palindrome = Palindrome(last_service_mileage, warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 3000
        warning_light_is_on = False
        palindrome = Palindrome(last_service_mileage, warning_light_is_on)
        self.assertFalse(palindrome.needs_service())

class TestRorschach(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = '2023-03-01'
        rorschach = Rorschach(last_service_date)
        self.assertTrue(rorschach.needs_service())

    def test_does_not_need_service(self):
        last_service_date = '2023-07-01'
        rorschach = Rorschach(last_service_date)
        self.assertFalse(rorschach.needs_service())

class TestThovex(unittest.TestCase):
    def test_needs_service(self):
        last_service_mileage = 12000
        thovex = Thovex(last_service_mileage)
        self.assertTrue(thovex.needs_service())

    def test_does_not_need_service(self):
        last_service_mileage = 8000
        thovex = Thovex(last_service_mileage)
        self.assertFalse(thovex.needs_service())

if __name__ == '__main__':
    unittest.main()
