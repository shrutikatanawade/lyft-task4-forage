# thovex.py

# thovex.py

from datetime import datetime
from engine.capulet_engine import CapuletEngine

class Thovex(CapuletEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

    def engine_should_be_serviced(self):
        # Compare last_service_mileage with the Thovex engine service interval (60,000 miles)
        # Return True if the engine needs service, otherwise False
        thovex_service_interval = 60000
        if self.current_mileage - self.last_service_mileage > thovex_service_interval:
            return True
        else:
            return False
