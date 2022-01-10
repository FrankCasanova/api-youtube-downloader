from fastapi import APIRouter
from starlette import status

from .views import download_audio_view


router = APIRouter(prefix="/api")

router.add_api_route(
    "/download",
    endpoint=download_audio_view,
    methods=["POST"],
    status_code=status.HTTP_200_OK,
    summary="Download audio from youtube",
    tags=["downloader"],
)
