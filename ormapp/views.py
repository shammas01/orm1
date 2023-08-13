from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import Chapter
from rest_framework.response import Response
from . serializers import ListSerializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.


class ChapterView(APIView):
    def get(self,request, format=None):
        list_user = Chapter.objects.all()
        serializer = ListSerializer(list_user, many=True)
        return Response(serializer.data)
    

    def post(self, request,format=None):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
