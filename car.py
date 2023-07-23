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
