import youtube_dl


def get_download_links(event, context):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(event['url'], download=False)
    return result
