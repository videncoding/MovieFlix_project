from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    Movie_ID = models.IntegerField(default=0, unique=True)
    Title = models.CharField(max_length=50)
    Poster = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    IMDB_Rating = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    User_ID = models.IntegerField(default = 0, unique=True, primary_key=True)
    Role = models.CharField(max_length=20, blank=True)
    Genres = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.First_Name + self.Last_Name
class Comment(models.Model):
    Comment_ID = models.IntegerField(default=0, unique=True)
    User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Comment = models.CharField(max_length=200)
    def __str__(self):
        return "{}: Comment {}".format(self.Movie_ID, self.Comment_ID)



class Rating(models.Model):
    Rating_ID = models.IntegerField(default=0, unique=True)
    Movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    User_Rating = models.IntegerField(default=0)

    def __str__(self):
        return "{}: Rating {}".format(self.Movie_ID, self.Rating_ID)

class WatchedList(models.Model):
    WatchedList_ID = models.IntegerField(default=0, unique=True)
    User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return "Watched list of user {}".format(self.User_ID)