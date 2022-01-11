from os import path

from fastapi.responses import RedirectResponse
from pytube import YouTube


def download_audio_yt(url: str):
    try:
        yt = YouTube(url)

        stream = yt.streams.filter(only_audio=True).first()

        file = stream.download(
            skip_existing=True,
            filename_prefix="FRNKCSNV_",
            filename=f"{yt.title}.mp3",
            output_path="downloads/",
        )

        return file

    except Exception as e:
        print(e)
        return RedirectResponse(
            url="/error", status_code=302, headers={"Location": msg}
        )
