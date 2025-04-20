from rest_framework import serializers
from django.db import models
from .models import Actor, Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'character', 'image']

class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(queryset=Actor.objects.all(), slug_field='name', many=True)
    
    class Meta:
        model = Movie
        fields=['id', 'title', 'release_year', 'actors']