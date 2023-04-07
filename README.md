# Youtube playlist download script

This repository contains python script that makes downloading batch of YouTube videos simple and fast.

## Using the script

Open your Terminal and navigate to location where you want to clone this repository.

1. Clone repository by executing command ```git clone https://github.com/mattdmv/youtube-playlist-download.git```.
2. Enter cloned repository by executing command ```cd youtube-playlist-download```.
3. Create new ```conda``` envirnoment from ```environment.yaml``` file by executing command ```conda env create -f environment.yaml```. 
   New conda environment named ```pytube-only``` will be created from the ```environment.yaml``` containing all the necessary packages 
   to run the script.
4. Activate previously created conda environment by executing command ```conda activate pytube-only```.

Next, it will be needed to create environment variables YT_PLAYLIST_URL and YT_DOWNLOAD_LOC. The script is using those variables 
to run properly. You could also hard code those in the script and skip next steps. The reason I have those as environment variables 
is beacuse I am always downloading videos from the same YouTube playlist and I have dedicated location where I want videos to be downloaded 
at.

1. Execute ```vim ~/.bash_profile```.
2. Insert (press ```I```):
```
export YT_PLAYLIST_URL="<your playlist url>"
export YT_DOWNLOAD_PATH="<path to a folder you want videos to be downloaded at>"
```
3. Save and exit ```~/.bash_profile``` (press ```ESC```, then type ```:wq```).
4. Execute ```vim ~/.profile``` or ```vim ~/.zprofile``` (if you are using Oh My Zsh) and insert (press ```I```):
```
source ~/.bash_profile
```
5. Save and exit ```~/.profile``` or ```~/.zprofile``` (press ```ESC```, then type ```:wq```).
6. Restart your terminal app for this variables to be permanently available. After restarting you can check if they are available by running 
   ```env``` command in your terminal. Search for them among other environment variables from the output.

Finally, everything should be set up to run the script and download videos from the provided playlist.

Execute ```python main.py``` and wait until all videos are downloaded.
