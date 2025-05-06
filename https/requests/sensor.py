from datetime import datetime

from pydantic import BaseModel, Field

class Sensor(BaseModel):
    temperature: float = 0
    humidity: float = 0
    isMotionDetected: bool = False
    gasLevel: int = 0,
    isGasDetected: bool = False,
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

    model_config = {
        "json_schema_extra": {
            "example": {
                "temperature": 22.5,
                "humidity": 65.2,
                "gasLevel": 430,
                "isMotionDetected": False,
                "isGasDetected": False
            }
        }
    }