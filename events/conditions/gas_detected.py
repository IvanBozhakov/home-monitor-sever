from https.requests.sensor import Sensor
from .condition import Condition

class GasDetected(Condition):
    def __init__(self, sensor: Sensor):
        self._sensor = sensor

    def check(self) -> bool:
        return self._sensor.isGasDetected
    
    def __str__(self):
        return f"Gas was detected\n"