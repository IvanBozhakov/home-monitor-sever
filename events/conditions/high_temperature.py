from https.requests.sensor import Sensor
from .condition import Condition

class HighTemperature(Condition):
    def __init__(self, sensor: Sensor):
        self._sensor = sensor

    def check(self) -> bool:
        return self._sensor.temperature > 60
    
    def __str__(self):

        return f"Too high temp detected {self._sensor.temperature}°\n"