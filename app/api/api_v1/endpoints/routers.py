from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status
from ....core.config import EPISODELIST_ENDPOINT, PODCASTLIST_ENDPOINT
import httpx

router = APIRouter(tags=["podcast"])


@router.get("/podcastlist", status_code=status.HTTP_200_OK)
async def podcastlist():
    async with httpx.AsyncClient() as client:
        response = await client.get(PODCASTLIST_ENDPOINT)
    return response.json()


@router.get("/episodelist", status_code=status.HTTP_200_OK)
async def podcastlist():
    async with httpx.AsyncClient() as client:
        response = await client.get(EPISODELIST_ENDPOINT)
    return response.json()
