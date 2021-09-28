from typing import Any
from fastapi import APIRouter, HTTPException, status

from api.module.routes import route_service as service
from .route import Route, BaseResponse

router = APIRouter()


@router.post("/generate")
def generate_route(req: Route) -> Any:
    if req is None:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return service.generate_route(req)
