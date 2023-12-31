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
