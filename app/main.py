from fastapi import FastAPI
from .api.api_v1.endpoints.routers import router as podcast_router

app = FastAPI()
app.include_router(router=podcast_router, prefix="")
