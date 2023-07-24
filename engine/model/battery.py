# engine/model/battery.py

from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

class Spindler(Battery):
    def __init__(self):
        self.service_interval = 3  # Upgraded service interval from 2 to 3 years

class Battery:
    def __init__(self):
        self.service_interval = 2

    def needs_service(self, last_service_date):
        return (last_service_date is None) or (self._days_since_service(last_service_date) >= self.service_interval * 365)

    def _days_since_service(self, last_service_date):
        # Calculate the number of days since the last service date
        pass  # Replace this with the actual implementation


class Spindler(Battery):
    def __init__(self):
        self.service_interval = 3  # Upgraded service interval from 2 to 3 years


class CarriganTire:
    def needs_service(self, tire_wear):
        # Carrigan tires should be serviced if any of the values in the tire_wear array is >= 0.9
        return any(wear >= 0.9 for wear in tire_wear)


class OctoprimeTire:
    def needs_service(self, tire_wear):
        # Octoprime tires should be serviced if the sum of all values in the tire_wear array is >= 3
        return sum(tire_wear) >= 3
