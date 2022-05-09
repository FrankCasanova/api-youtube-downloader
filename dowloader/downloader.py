
from pytube import YouTube


def download_audio_yt(url: str):
    try:
        yt = YouTube(url)

        stream = yt.streams.get_audio_only('mp4')

        file = stream.download(
            skip_existing=True,
            filename_prefix="FRNKCSNV_",
            output_path="downloads/",
        )

        return file

    except Exception as e:
        return 'unafortunately, an error has occured, try again later'
