from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Actor, Movie
from .serializer import ActorSerializer, MovieSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser, FormParser

#here are all the actors functions
@extend_schema(request=ActorSerializer, responses=ActorSerializer)
@api_view(['GET'])
def get_actors(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

@extend_schema(request=ActorSerializer, responses=ActorSerializer)
@parser_classes([MultiPartParser, FormParser])
@api_view(['POST'])
def add_actor(request):
    parser_classes = (MultiPartParser, FormParser)
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=ActorSerializer, responses=ActorSerializer)
@parser_classes([MultiPartParser, FormParser])
@api_view(['POST'])
def add_actors(request):
    serializer = ActorSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=ActorSerializer, responses=ActorSerializer)
@parser_classes([MultiPartParser, FormParser])
@api_view(['PUT'])
def update_actor(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ActorSerializer(actor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=ActorSerializer, responses=ActorSerializer)
@api_view(['GET'])
def find_actor(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@extend_schema(request=ActorSerializer, responses=ActorSerializer)
@api_view(['DELETE'])
def delete_actor(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    actor.delete()
    return Response("actor deleted")

#here are all the movie functions
# get_movies
# add_movie
# add_movies
# find_movie

@extend_schema(request=MovieSerializer, responses=MovieSerializer)
@api_view(['GET'])
def get_movies(request):
    actors = Movie.objects.all()
    serializer = MovieSerializer(actors, many=True)
    return Response(serializer.data)

@extend_schema(request=MovieSerializer, responses=MovieSerializer)
@parser_classes([MultiPartParser, FormParser])
@api_view(['POST'])
def add_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=MovieSerializer, responses=MovieSerializer)
@parser_classes([MultiPartParser, FormParser])
@api_view(['POST'])
def add_movies(request):
    serializer = MovieSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=MovieSerializer, responses=MovieSerializer)
@api_view(['GET'])
def find_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@extend_schema(request=MovieSerializer, responses=MovieSerializer)
@parser_classes([MultiPartParser, FormParser])
@api_view(['PUT'])
def update_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=MovieSerializer, responses=MovieSerializer)
@api_view(['GET'])
def find_moviebyactor(request, actor):
    try:
        actor_obj = Actor.objects.get(name=actor)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    movies = Movie.objects.filter(actors=actor_obj)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@extend_schema(request=MovieSerializer, responses=MovieSerializer)
@api_view(['DELETE'])
def delete_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    movie.delete()
    return Response("movie deleted")