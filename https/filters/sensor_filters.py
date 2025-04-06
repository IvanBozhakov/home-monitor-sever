from datetime import datetime
from functools import wraps
from typing import List

from fastapi import Request, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


def sort(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")
        sort_order = request.query_params.get("sort", "asc").lower()
        sensors: List[dict] = kwargs.get("sensors", [])

        if not sensors:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No sensor data found.")

        if sort_order == "desc":
            sensors.sort(key=lambda x: datetime.fromisoformat(x["timestamp"]), reverse=True)
        else:
            sensors.sort(key=lambda x: datetime.fromisoformat(x["timestamp"]), reverse=False)

        kwargs["sensors"] = sensors
        return await func(*args, **kwargs)

    return wrapper


def limit(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")
        limit_value = request.query_params.get("limit", None)

        sensors: List[dict] = kwargs.get("sensors", [])

        if limit_value is not None:
            try:
                limit_value = int(limit_value)
                if limit_value < 1:
                    raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Limit must be greater than 0.")
            except ValueError:
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid limit value. Must be an integer.")

            sensors = sensors[:limit_value]

        kwargs["sensors"] = sensors
        return await func(*args, **kwargs)

    return wrapper

def between_dates(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")
        sensors: List[dict] = kwargs.get("sensors", [])

        start_date_str = request.query_params.get("start_date", None)
        end_date_str = request.query_params.get("end_date", None)

        start_date = None
        end_date = None
        try:
            if start_date_str:
                start_date = datetime.fromisoformat(start_date_str)
            if end_date_str:
                end_date = datetime.fromisoformat(end_date_str)
        except ValueError:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid date format. Use ISO 8601 format.")

        filtered_sensors = []
        for sensor in sensors:
            sensor_timestamp = datetime.fromisoformat(sensor["timestamp"])

            if start_date and sensor_timestamp < start_date:
                continue
            if end_date and sensor_timestamp > end_date:
                continue

            filtered_sensors.append(sensor)

        kwargs["sensors"] = filtered_sensors
        return await func(*args, **kwargs)

    return wrapper