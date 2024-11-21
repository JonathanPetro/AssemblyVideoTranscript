
from assembly_functions import *
from audio_extracter import convert_video_to_audio

def video_to_transcript(input_video):
    convert_video_to_audio(input_video, "audio.mp3")

    filename = "audio.mp3"
    audio_url = upload(filename)

    save_transcript(audio_url, 'video-transcript')

