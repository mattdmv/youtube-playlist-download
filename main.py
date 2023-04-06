from pytube import Playlist
from tqdm import tqdm

# create Playlist object and give URL of playlist 
playlist = Playlist('https://youtube.com/playlist?list=PLtywwzgW29LIhTsH4QYttpivvkIaByV25')

# print the title of the playlist 
#print(playlist.title)

# print URLs of the videos in the playlist
for url in playlist.video_urls:
	print(url)

# download videos with the highest quality
for video in tqdm(playlist.videos):
    print('Downloading: ', video.title)
    video.streams.get_highest_resolution().download()