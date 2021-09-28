from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": "Something went wrong", "errors": [exc.detail]}
    )
