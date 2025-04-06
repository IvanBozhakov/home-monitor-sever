from fastapi import FastAPI, Depends, HTTPException
from auth.verify import verify_token
from https.handlers.error import http_exception_handler
from https.routes import hub_routes

app = FastAPI(
    dependencies=[Depends(verify_token)],
    title="Local home server",
    description="A local server used for communication with home devices.",
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

app.add_exception_handler(HTTPException, handler=http_exception_handler)
app.include_router(hub_routes.router, prefix="/device", tags=["Device"])
