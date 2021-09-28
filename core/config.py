from pydantic import BaseSettings, AnyHttpUrl, validator
from typing import List, Union
from starlette.config import Config
from starlette.datastructures import Secret


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ARC"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    config = Config(".env")

    DEBUG: bool = config("DEBUG", cast=bool, default=False)
    SECRET_KEY: Secret = config("SECRET_KEY", default="r@nD0m", cast=Secret)

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
