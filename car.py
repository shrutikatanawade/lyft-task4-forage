# car.py
from engine.model.engine import Engine
from engine.model.battery import Battery

class Car:
    def __init__(self, name, last_service_date, engine, battery):
        self.name = name
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

class Tire:
    def __init__(self, tire_type):
        self.type = tire_type

    def needs_service(self, tire_wear_array):
        if self.type == "Carrigan":
            # Carrigan tires need service if any value in the tire wear array is >= 0.9
            return any(wear >= 0.9 for wear in tire_wear_array)
        elif self.type == "Octoprime":
            # Octoprime tires need service if the sum of all values in the tire wear array is >= 3
            return sum(tire_wear_array) >= 3
        else:
            raise ValueError("Invalid tire type")
