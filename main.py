from pytube import Playlist
import os

playlist_url = os.environ["YT_PLAYLIST_URL"]

# create Playlist object and give URL of playlist 
playlist = Playlist(playlist_url)

# print the title of the playlist 
#print(playlist.title)

# print URLs of the videos in the playlist
for url in playlist.video_urls:
	print(url)

# download videos with the highest quality
for video in playlist.videos:
    print('Downloading: ', video.title)
    video.streams.get_highest_resolution().download()