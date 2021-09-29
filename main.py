import uvicorn

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from src.api.api import api_router
from src.core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from src.core.exception import http_error_handler


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)
    return application


# app = get_application()

if __name__ == "__main__":
    uvicorn.run(get_application(), host="0.0.0.0", port=8848)
