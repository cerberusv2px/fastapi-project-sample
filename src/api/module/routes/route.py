from pydantic import BaseModel
from typing import List, Optional


class Outlet(BaseModel):
    id: int
    lat: float
    lng: float
    name: str
    category: str
    categoryId: int
    channel: str
    channelId: int
    town: str
    townId: int
    distance: Optional[float] = 0.0


class Route(BaseModel):
    dse_count: int
    outlets: List[Outlet]
    max_outlet: int
    capacity: List[int]


class RouteResponse(BaseModel):
    dse: int
    distance: float
    travel: List[Outlet]


class BaseResponse(BaseModel):
    success: bool
    data: List[RouteResponse]
