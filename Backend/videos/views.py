from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.youtube import search_youtube_videos
from .services.classifier import classify_text


@api_view(["GET"])
def search_videos(request):
    query = request.GET.get("q", "").strip()

    if not query:
        return Response({
            "query": "",
            "results": []
        })

    youtube_videos = search_youtube_videos(
        query,
        max_results=10
    )

    educational_videos = []

    for video in youtube_videos:
        classification = classify_text(
            video["title"]
        )

        if classification["educational"]:
            video["educational_score"] = (
                classification["score"]
            )

            educational_videos.append(video)

    educational_videos.sort(
        key=lambda video: video["educational_score"],
        reverse=True
    )

    return Response({
        "query": query,
        "results": educational_videos
    })