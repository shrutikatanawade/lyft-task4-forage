# sternman_engine.py

from engine.model.engine import Engine

class SternmanEngine(Engine):
    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
