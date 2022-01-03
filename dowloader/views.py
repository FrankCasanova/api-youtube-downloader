from fastapi.param_functions import Form
from .downloader import download_audio
from fastapi import Request, Form, File


async def download_audio_view(request: Request, url: str = Form(...)) -> File:
    print(request.headers)
    return download_audio(url)
