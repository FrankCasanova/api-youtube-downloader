from moviepy.editor import VideoFileClip


def convert_to_mp3(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    return audio_path
