from rest_framework import serializers
from . models import Chapter


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
