import os
import youtube_dl      

ydl_opts = {}
ydl = youtube_dl.YoutubeDL(ydl_opts)

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

os.chdir('music/english/')


# Downloading all songs in each playlist 

# Downloading video and audio streams: https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command
# Getting video links from playlist: https://stackoverflow.com/questions/43910501/how-do-i-retrieve-individual-video-urls-from-a-playlist-using-youtube-dl-within

for directory, link in urls.items():

    with ydl:
        result = ydl.extract_info(link, download = False)

        if 'entries' in result:
            playlist = result['entries']

            for i, item in enumerate(playlist):
                video_url = result['entries'][i]['webpage_url']

                print(os.curdir)
                os.chdir(f"{directory}")
                command = f"ffmpeg -ss 00:00:30.00 -i "OUTPUT-OF-FIRST URL" -t 00:00:30.00 -c copy out.mp4"
                os.system(command)
                os.chdir("../")



# Looping through all songs and extracting 00:00:30 to 00:01:00 and putting into new directories
for directory in urls.keys():
    for filename in os.listdir(directory):
        