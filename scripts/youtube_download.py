import os

urls = {'70s_music': 'https://www.youtube.com/watch?v=N43mbd4qaHc&list=PLUcVRPQ0oeIqUZ_rMMg3FVxKl16g76CH5',
        '80s_music': 'https://www.youtube.com/watch?v=bVey-358Vcc&list=PL85813B7453734CFB',
        '90s_music': 'https://www.youtube.com/watch?v=m4oXDxPFT_s&list=PLcMd4zmqZWkDs_CMg1iDRgWePxn9_FXBw',
        '00s_music': 'https://www.youtube.com/watch?v=SvAQAeLa-jY&list=PLW_aX2Vduw-sQTQDdmL7TdEiL_X8ldMyQ-',
        '10s_music': 'https://www.youtube.com/watch?v=kn6-c223DUU&list=PL7Q2ZklqtR8B_EAUfXt5tAZkxhCApfFkL'}

for directory, link in urls.items():
    command = f"youtube-dl -o --playlist-end 100 ../music/english/{directory} {link}"
    print(command)
    #os.system("youtube-dl -o ")