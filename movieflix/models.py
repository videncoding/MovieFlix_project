from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    Movie_ID = models.IntegerField(default=0, unique=True, primary_key=True)
    Title = models.CharField(max_length=50)
    Poster = models.CharField(max_length=50)
    Description = models.CharField(max_length=2000)
    IMDB_Rating = models.FloatField(default=0)
    User_Rating = models.FloatField(default=0)
    objects = models.Manager()


class UserProfile(models.Model):
    User_ID = models.AutoField(primary_key=True)
    Email = models.EmailField(default=0, unique=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=150)
    Password = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False, blank=True)
    Genres = models.CharField(max_length=20, blank=True)
    objects = models.Manager()


class Comment(models.Model):
    Comment_ID = models.AutoField(primary_key=True)
    User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Comment = models.CharField(max_length=200)
    objects = models.Manager()


class Rating(models.Model):
    Rating_ID = models.AutoField(primary_key=True)
    Movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    User_Rating = models.FloatField(default=0)
    objects = models.Manager()


class WatchedList(models.Model):
    WatchedList_ID = models.AutoField(primary_key=True)
    User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    objects = models.Manager()
