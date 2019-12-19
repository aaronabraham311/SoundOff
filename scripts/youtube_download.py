import os

urls = {'70s_music': 'https://www.youtube.com/playlist?list=PLUcVRPQ0oeIqUZ_rMMg3FVxKl16g76CH5',
        '80s_music': 'https://www.youtube.com/playlist?list=PL85813B7453734CFB',
        '90s_music': 'https://www.youtube.com/playlist?list=PLcMd4zmqZWkDs_CMg1iDRgWePxn9_FXBw',
        '00s_music': 'https://www.youtube.com/playlist?list=PL05E1623111A9A860',
        '10s_music': 'https://www.youtube.com/playlist?list=PL7Q2ZklqtR8B_EAUfXt5tAZkxhCApfFkL'}

os.chdir('music/english/')

for directory, link in urls.items():
    print(os.curdir)
    os.chdir(f"{directory}")
    command = f"youtube-dl -i -f mp4 --yes-playlist {link}"
    os.system(command)
    os.chdir("../")