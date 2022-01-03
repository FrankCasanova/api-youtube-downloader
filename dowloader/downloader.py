from pytube import YouTube


def download_audio(url: str):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(
            only_audio=True).first()

        file = stream.download(
            skip_existing=True,
            filename_prefix="FRNKCSNV_",
        )

        return file

    except Exception as e:
        print(e)
        return {"error": f"Error while downloading: {e}"}
