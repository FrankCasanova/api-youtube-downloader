import os
from multiprocessing import Process

from fastapi import Form
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from cleaner import cleaner

templates = Jinja2Templates(directory="templates")

from .downloader import download_audio_yt


async def download_audio_view(request: Request, url: str = Form(...)) -> FileResponse:

    try:

        file = download_audio_yt(url)

        Process(target=cleaner).start()

        return FileResponse(file, media_type="audio/mpeg", filename=f"{file}")

    except Exception as e:
        msg: str = "Please enter a valid youtube url"
        return RedirectResponse(
            url="/error", status_code=302, headers={"Location": msg}
        )
