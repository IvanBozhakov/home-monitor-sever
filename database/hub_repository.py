from database.repository import Repository

from https.requests.sensor import Sensor

class HubRepository(Repository):
    def __init__(self, hub: str):
        super().__init__()
        self.collection = self.db.table(hub)
        
    def add(self, sensor: Sensor):
        self.collection.insert(sensor.model_dump())

    def get_last(self):
        result = self.collection.all()
        if result:
            return max(result, key=lambda x: x['timestamp'])

        return None

    def get_all(self):
        return self.collection.all()