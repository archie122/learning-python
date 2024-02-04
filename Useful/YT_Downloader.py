from pytube import Playlist
import ssl

# Bypass SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

x = input("Enter Playlist URL: ")

playlist = Playlist(x)
print("Total videos in playlist: ", len(playlist.video_urls))

for video in playlist.videos:
    stream = video.streams.get_highest_resolution()
    print("Downloading: ", video.title)
    stream.download()


# # importing packages
# from pytube import YouTube
# import os
#
# # url input from user
# yt = YouTube(
#     str(input("Enter the URL of the video you want to download: \n>> ")))
#
# # extract only audio
# video = yt.streams.filter(only_audio=True).first()
#
# # check for destination to save file
# print("Enter the destination (leave blank for current directory)")
# destination = str(input(">> ")) or '.'
#
# # download the file
# out_file = video.download(output_path=destination)
#
# # save the file
# base, ext = os.path.splitext(out_file)
# new_file = base + '.mp3'
# os.rename(out_file, new_file)
#
# # result of success
# print(yt.title + " has been successfully downloaded.")
