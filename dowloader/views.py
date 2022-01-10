from fastapi import File
from fastapi import Form
from fastapi import Request
from fastapi.param_functions import Form

from .downloader import download_audio_yt


async def download_audio_view(request: Request, url: str = Form(...)) -> File:
    print(request.headers)
    print(url)

    if "youtube" in url:
        return download_audio_yt(url)
