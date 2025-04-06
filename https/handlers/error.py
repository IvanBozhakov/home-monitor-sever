from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def http_exception_handler(request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail), "code": exc.status_code},
        headers=exc.headers,
    )