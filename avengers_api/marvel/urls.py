from django.urls import path
from .views import get_actors, add_actor, add_actors, find_actor, get_movies, add_movie, add_movies, find_movie, find_moviebyactor, delete_actor, delete_movie, update_actor, update_movie

urlpatterns = [
    path('actors/', get_actors, name='get_actos'),
    path('actors/add/', add_actor, name='add_actor'),
    path('actors/add_many/', add_actors, name='add_actors'),
    path('actors/find/<int:pk>', find_actor, name='find_actor'),
    path('actors/delete/<int:pk>', delete_actor, name='delete_actor'),
    path('actors/update/<int:pk>', update_actor, name='update_actor'),
    path('movies/', get_movies, name='get_movies'),
    path('movies/add/', add_movie, name='add_movie'),
    path('movies/add_many/', add_movies, name='add_movies'),
    path('movies/find_by_actor/<str:actor>', find_moviebyactor, name='find_moviebyactor'),
    path('movies/find/by-id/<int:pk>', find_movie, name='find_movie'),
    path('movies/delete/<int:pk>', delete_movie, name='delete_movie'),
    path('movies/update/<int:pk>', update_movie, name='update_movie'),
    
]