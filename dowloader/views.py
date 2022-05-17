from multiprocessing import Process

from fastapi import Form
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .conversor import convert_to_mp3
from cleaner import cleaner

templates = Jinja2Templates(directory="templates")

from .downloader import download_audio_yt


async def download_audio_view(request: Request, url: str = Form(...)) -> FileResponse:

    file = download_audio_yt(url)

    if "unafortunately" in file:
        return RedirectResponse(url="/error", status_code=302)

    Process(target=cleaner).start()

    mp3 = convert_to_mp3(file, file.replace(".mp4", ".mp3"))

    return FileResponse(
        mp3, media_type="audio/MPEG-1", filename=f"{mp3.split('/')[-1]}"
    )

    # msg: str = "Please enter a valid youtube url"
    # return RedirectResponse(
    #     url="/error", status_code=302, headers={"Location": msg}
    # )
