from typing import Optional

from fastapi import Query

class FetchSensorsQuery:
    def __init__(
        self,
        sort: Optional[str] = Query(None, description="Sort sensors data ASC/DESC"),
        limit: Optional[int] = Query(None, description="Limit number"),
        start_date: Optional[str] = Query(None, description="Start date of event ISO 8601"),
        end_date: Optional[str] = Query(None, description="End date of event ISO 8601"),
    ):
        self.sort = sort
        self.limit = limit
        self.start_date = start_date
        self.end_date = end_date

    model_config = {
        "json_schema_extra": {}
    }