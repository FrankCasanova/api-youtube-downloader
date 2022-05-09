from multiprocessing import Process
import os

from fastapi import Form
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from cleaner import cleaner

templates = Jinja2Templates(directory="templates")

from .downloader import download_audio_yt


async def download_audio_view(request: Request, url: str = Form(...)) -> FileResponse:

    file = download_audio_yt(url)

    if 'unafortunately' in file:
        return RedirectResponse(
            url="/error", status_code=302
        )

    base, ext = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)

    Process(target=cleaner).start()

    return FileResponse(new_file, media_type='audio/*', filename=f"{file}")

    # msg: str = "Please enter a valid youtube url"
    # return RedirectResponse(
    #     url="/error", status_code=302, headers={"Location": msg}
    # )
