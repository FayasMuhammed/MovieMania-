from rest_framework import serializers
from movie.models import *



class Genre_serializer(serializers.ModelSerializer):
    class Meta:
        model=Genre_model
        fields="__all__"


class Movie_serializer(serializers.ModelSerializer):
    class Meta:
        model=Movie_model
        fields="__all__"