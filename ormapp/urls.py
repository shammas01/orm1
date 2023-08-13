from django.urls import path
from . views import ChapterView

urlpatterns = [
    path('chapter/',ChapterView.as_view())
]
