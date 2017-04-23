from __future__ import unicode_literals
import youtube_dl
'''import pafy, youtube_dl
url = "https://www.youtube.com/watch?v=h2VbU22H1g8"
video = pafy.new(url)
print video.streams'''

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=h2VbU22H1g8',
        download=False # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
video_url = video['url']
print(video_url)
