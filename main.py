import uvicorn, logging

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from api.api import api_router
from core.config import settings
from core.exception import http_error_handler

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = FastAPI(
    title=settings.PROJECT_NAME
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.add_exception_handler(HTTPException, http_error_handler)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8848)
