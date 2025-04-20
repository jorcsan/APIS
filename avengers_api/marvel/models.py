from django.db import models

# this is the actor model.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
#this is the movie model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title