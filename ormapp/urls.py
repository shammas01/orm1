from django.urls import path
from . views import UserView

urlpatterns = [
    path('chapter/',UserView.as_view())
]
