import os
import shutil
import re

'''
Bollywood and Malayalam directories
'''

# Playlist of songs
urls = {'bollywood_videos': 'https://www.youtube.com/playlist?list=PLvczmdAAtKHsHZY1koKHzKNwsOq82mYD0',
        'malayalam_videos': 'https://www.youtube.com/playlist?list=PLiY_ozoWy_l73yd3LlALYkVmRc8q9rR_l',}
soundbite_directories = ['bollywood_audio', 'malayalam_audio']


# Downloading all songs in each playlist 

# I have decided that downloading the videos and then cutting it up is much more time efficient than using the above links.
os.chdir('music/indian')

for directory, link in urls.items():
    os.system(f"mkdir {directory}")
    os.chdir(f"{directory}")
    command = f"youtube-dl --extract-audio --audio-format mp3 -i {link}"
    os.system(command)
    os.chdir("../")

# Creating directories for audio bites
for directory_name in soundbite_directories:
    os.system(f"mkdir {directory_name}")

# Renaming files to remove all non-alphanumeric characters

for directory in urls.keys():
    os.chdir(f"{directory}")
    for filename in os.listdir():
        os.rename(filename, re.sub('[\W_]+','',filename))
    os.chdir("../")

# Getting 2 30-sec soundbites from 00:00:30 - 00:01:00 and 00:01:30 - 00:02:00
for i, directory in enumerate(urls.keys()):
    os.chdir(f"{directory}")
    for filename in os.listdir():
        command1 = f"ffmpeg -ss 00:00:30.00 -i {filename} -t 00:00:30.00 -c copy ../{soundbite_directories[i]}/{filename}_1.mp3"
        command2 = f"ffmpeg -ss 00:01:30.00 -i {filename} -t 00:00:30.00 -c copy ../{soundbite_directories[i]}/{filename}_2.mp3"
        os.system(command1)
        os.system(command2)
    os.chdir("../")

# Removing all full audio directories
for directory in urls.keys():
    shutil.rmtree(directory) 