from pytube import Playlist
import os
from tqdm import tqdm

playlist_url = os.environ["YT_PLAYLIST_URL"]
output_path = os.environ["YT_DOWNLOAD_LOC"]

# create Playlist object and give URL of playlist 
playlist = Playlist(playlist_url)

# print the title of the playlist 
# print(playlist.title)

# print URLs of the videos in the playlist
# for url in playlist.video_urls:
# 	print(url)

# download videos with the highest quality
for video in tqdm(playlist.videos):
    print('Downloading: ', video.title)
    video.streams.get_highest_resolution().download(output_path=output_path)