from __future__ import unicode_literals
import youtube_dl

def lambda_handler(event, context):
    # TODO implement
	ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
	with ydl:
		result = ydl.extract_info(
        event['url'],
        download=False # We just want to extract the info
    	)
	if 'entries' in result:
		# Can be a playlist or a list of videos
		video = result['entries'][0]
	else:
		# Just a video
		video = result
	return video
