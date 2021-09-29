from fastapi import APIRouter
import src.api.module.routes as routes

api_router = APIRouter()
api_router.include_router(routes.route_controller.router, prefix="/routes", tags=["routes"])
