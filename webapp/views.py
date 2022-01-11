from fastapi import File
from fastapi import Form
from fastapi import Request
from fastapi.templating import Jinja2Templates

from dowloader.downloader import download_audio_yt

templates = Jinja2Templates(directory="templates")


def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


def downloader_app(request: Request, url: str = Form(...)):
    if "youtube.com/watch?v=" in url:
        msg = "Thanks for use our service"
        file = download_audio_yt(url)
        return templates.TemplateResponse(
            "msg.html", {"request": request, "file": file, "msg": msg}
        )

    else:
        msg = "Please enter a valid youtube url"
        return templates.TemplateResponse("msg.html", {"request": request, "msg": msg})


def error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})
