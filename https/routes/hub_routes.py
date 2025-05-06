from typing import List, Set
from fastapi import APIRouter, Request, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from database.hub_repository import  HubRepository, Repository
from events.conditions.gas_detected import GasDetected
from events.conditions.high_temperature import HighTemperature
from events.warning import WarningEvent
from https.queries.fetch_sensors_query import FetchSensorsQuery
from https.requests.sensor import Sensor
from events.conditions.scheduler import Scheduler as ConditionScheduler
from https.filters import sensor_filters

router = APIRouter()

""" Post sensor data """
@router.post(
    "/{hub}/create",
    responses={
        HTTP_201_CREATED: {
            "description": "Successfully created record",
            "content": {
                "application/json": {
                    "example": {
                        "status_code": HTTP_201_CREATED,
                        "data": {
                            "temperature": 25.0,
                            "humidity": 50.0,
                            "isMotionDetected": False,
                            "gasLevel": 0,
                            "isGasDetected": True,
                            "timestamp": "2025-03-23T18:27:35.204931"
                        }
                    }
                }
            }
        }
    },
    status_code=HTTP_201_CREATED
)
async def post_sensor_data(hub: str, sensor: Sensor):
    scheduler = ConditionScheduler([GasDetected(sensor), HighTemperature(sensor)])
    scheduler.on_true(WarningEvent())

    data = HubRepository(hub)
    data.add(sensor)
    return {"status_code": HTTP_201_CREATED, "data": sensor}


""" Fetch sensor data and applying filters """
@router.get(
    "/{hub}/get",
    responses={
        HTTP_200_OK: {
            "description": "Successfully retrieved sensor data",
            "content": {
                "application/json": {
                    "example": {
                        "status_code": HTTP_200_OK,
                        "data": [
                            {
                                "temperature": 22.5,
                                "humidity": 65.2,
                                "isMotionDetected": False,
                                "gasLevel": 0,
                                "isGasDetected": False,
                                "timestamp": "2025-03-23T14:07:17.870819"
                            },
                            {
                                "temperature": 25.0,
                                "humidity": 60.0,
                                "isMotionDetected": False,
                                "gasLevel": 0,
                                "isGasDetected": False,
                                "timestamp": "2025-03-23T15:07:17.870819"
                            }
                        ]
                    }
                }
            }
        }
    },
)
@sensor_filters.sort
@sensor_filters.between_dates
@sensor_filters.limit
async def get_sensor_data(
        hub: str,
        request: Request,
        params: FetchSensorsQuery = Depends(),
        sensors: List[Sensor] = Depends(lambda hub: HubRepository(hub).get_all())
):
    return {"status_code": HTTP_200_OK, "data": sensors}

""" Fetch all hubs """
@router.get(
    "/hubs",
        responses={
                HTTP_200_OK: {
                    "description": "Successfully retrieved sensor data",
                    "content": {
                        "application/json": {
                            "example": {
                                "status_code": HTTP_200_OK,
                                "data": [
                                    "hub1",
                                    "hub2"
                                ]
                            }
                        }
                    }
                }
        },
)
async def get_hubs(hubs: Set[str] = Depends(lambda : Repository().get_hubs())):
    return {"status_code": HTTP_200_OK, "data": hubs}