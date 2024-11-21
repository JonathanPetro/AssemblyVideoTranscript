import subprocess

#make sure to specify what extension the output file has, this changes whether or not is is .mp3 or .wav or whatever else
def convert_video_to_audio(input_file, output_file):
    ffmpeg_cmd = [
       'ffmpeg',
        '-i', input_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ar', '44100',
        '-ac', '2',
        output_file
    ]

    try: 
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted!")
    except subprocess.CalledProcessError as e: 
        print("Conversion failed!")