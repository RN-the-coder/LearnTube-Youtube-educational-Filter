from django.urls import path
from .views import search_videos

urlpatterns = [
    path("search/", search_videos, name="search-videos"),
]