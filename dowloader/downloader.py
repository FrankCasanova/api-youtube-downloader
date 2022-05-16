from pytube import YouTube


def download_audio_yt(url: str):
    try:
        yt = YouTube(url)

        stream = yt.streams.filter(file_extension="mp4", res="360p").first()

        file = stream.download(
            skip_existing=True,
            filename_prefix="FRNKCSNV_",
            output_path="downloads/",
        )

        return file

    except Exception:
        return "unafortunately, an error has occured, try again later"
