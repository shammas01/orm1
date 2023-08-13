from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import Chapter
from rest_framework.response import Response
from . serializers import ListSerializer,ChapterUpdateSerializer
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


class ChapterEditView(APIView):
    # def get(self,request, format=None):
    #     list_user = Chapter.objects.all()
    #     serializer = ListSerializer(list_user, many=True)
    #     return Response(serializer.data)
    
    # def put(self, request,format=None):
    #     chapter = request.data
    #     serializer = ChapterUpdateSerializer(chapter,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'chapter edited'})
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):  # Updated parameter: chapter_id
        try:
            chapter = Chapter.objects.get(pk=pk)
        except Chapter.DoesNotExist:
            return Response({'msg': 'Chapter not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChapterUpdateSerializer(chapter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Chapter edited'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)