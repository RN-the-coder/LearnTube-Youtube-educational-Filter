from django.conf import settings
from googleapiclient.discovery import build


def search_youtube_videos(query, max_results=10):
    youtube = build(
        "youtube",
        "v3",
        developerKey=settings.YOUTUBE_API_KEY
    )

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    )

    response = request.execute()

    videos = []

    for item in response.get("items", []):
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]

        videos.append({
            "video_id": video_id,
            "title": snippet["title"],
            "description": snippet["description"],
            "channel": snippet["channelTitle"],
            "thumbnail": snippet["thumbnails"]["high"]["url"]
        })

    return videos