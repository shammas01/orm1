from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import Chapter
from rest_framework.response import Response
from . serializers import ListSerializer
from rest_framework.views import APIView
# Create your views here.


class UserView(APIView):
    def get(self,request):
        list_user = Chapter.objects.all()
        serializer = ListSerializer(list_user, many=True)
        return Response(serializer.data)