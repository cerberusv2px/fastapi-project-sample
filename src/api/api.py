from fastapi import APIRouter
import src.api.module.routes.route_controller as route_controller

api_router = APIRouter()
api_router.include_router(route_controller.router, prefix="/routes", tags=["routes"])
