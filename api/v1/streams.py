from fastapi import APIRouter
from typing import Optional
from fastapi.responses import FileResponse
import os

router = APIRouter()

MEDIA_DIR = os.getenv("MEDIA_DIR")



@router.get("/" , tags=["streams"])
async def get_stream(identifier : Optional[str] = None , isrc : Optional[str] = None) -> FileResponse:
    return MEDIA_DIR