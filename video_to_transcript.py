
from assembly_functions import *
from ffmpeg_to_assembly import video_to_transcript

filename = input("Input Video File Name: ")
if not filename:
    print("No video given, stopping script")
    exit()

video_to_transcript(filename)