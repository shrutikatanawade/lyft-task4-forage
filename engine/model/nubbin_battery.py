# engine/model/nubbin_battery.py

from engine.model.battery import Battery
from datetime import datetime, timedelta

class NubbinBattery(Battery):
    def needs_service(self):
        # Calculate the service threshold date based on the provided criteria (once every 4 years)
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)

        # Compare the current date with the service threshold date
        if datetime.today().date() >= service_threshold_date:
            return True
        else:
            return False
