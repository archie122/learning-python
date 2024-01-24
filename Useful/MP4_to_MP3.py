import os
from moviepy.video.io.VideoFileClip import VideoFileClip

os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"  # Replace with the actual path to ffmpeg executable


def convert_folder_to_mp3(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(output_folder, output_filename)

            convert_mp4_to_mp3(input_path, output_path)


def convert_mp4_to_mp3(input_path, output_path):
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio

    audio_clip.write_audiofile(output_path, codec='mp3')


if __name__ == "__main__":
    input_folder = "/Users/architchoudhary/Desktop/Music/Frank Sinatra/"  # Change this to the path of your input folder containing MP4 files
    output_folder = "/Users/architchoudhary/Desktop/Music/Frank Sinatra MP3/"  # Change this to the desired output folder path

    convert_folder_to_mp3(input_folder, output_folder)
