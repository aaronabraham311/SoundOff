import os
import shutil
import re

'''
70s music: 148 songs
80s music: 184 songs
90s music: 178 songs
00s music: 144 songs
10s music: 200 songs
'''

# Playlist of songs
urls = {'1970s_music_videos': 'https://www.youtube.com/playlist?list=PLGBuKfnErZlAkaUUy57-mR97f8SBgMNHh',
        '1980s_music_videos': 'https://www.youtube.com/playlist?list=PL90b28qTMGqIle4NmUvaAUtj20lAPETzE',
        '1990s_music_videos': 'https://www.youtube.com/playlist?list=PLZyqOyXxaVETqpHhT_c5GPmAPzhJpJ5K7',
        '2000s_music_videos': 'https://www.youtube.com/playlist?list=PLwW9XzYk5_cQyw-MDuD-bF-OCjJQ6UjZf',
        '2010s-music_videos': 'https://www.youtube.com/playlist?list=PLeZgwVkN7bbfVLcqnz9l5RjASqUkBtpBe'}
soundbite_directories = ['1970s_audio', '1980s_audio', '1990s_audio', '2000s_audio', '2010s_audio']


# Downloading all songs in each playlist 

# I have decided that downloading the videos and then cutting it up is much more time efficient than using the above links.
os.chdir('music/english/')

for directory, link in urls.items():
    print(os.curdir)
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