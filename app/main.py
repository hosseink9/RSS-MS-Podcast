from fastapi import FastAPI
import logging

from app.log.logging_lib import RouterLoggingMiddleware
from .api.api_v1.endpoints.routers import router as podcast_router
from app.core.config import logging_config

logging.config.dictConfig(logging_config)

app = FastAPI()
app.add_middleware(RouterLoggingMiddleware,
                   logger=logging.getLogger("elastic-logger"))
app.include_router(router=podcast_router, prefix="")
