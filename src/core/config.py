import logging
import sys

from datetime import datetime
from loguru import logger
from pydantic import AnyHttpUrl, validator
from typing import List, Union
from starlette.config import Config
from starlette.datastructures import Secret

from src.core.logger import InterceptHandler

API_PREFIX: str = "/api/v1"
PROJECT_NAME: str = "ARC"

BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", default="r@nD0m", cast=Secret)
VERSION: str = config("VERSION", default="1.0.0")

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
logger.add(f"log-{datetime.today().strftime('%Y-%m-%d')}.log", rotation="00:00", retention="30 days")

