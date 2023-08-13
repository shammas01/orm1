from django.urls import path
from . views import ChapterView, ChapterEditView

urlpatterns = [
    path('chapters/',ChapterView.as_view()),
    path('chapter/',ChapterEditView.as_view()),
    path('chapters/<int:pk>/',ChapterEditView.as_view())
]
