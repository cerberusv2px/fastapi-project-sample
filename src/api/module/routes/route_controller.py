from loguru import logger

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder

from . import route_service as service
from .route import Route, BaseResponse

router = APIRouter()


@router.post("/generate", response_model=BaseResponse)
def generate_route(req: Route) -> BaseResponse:
    if req is None:
        logger.error(f"{jsonable_encoder(req)} has an error")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return service.generate_route(req)
