from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.
class Movie(models.Model):
    Movie_ID = models.IntegerField(unique=True, primary_key=True)
    Title = models.CharField(max_length=50)
    Poster = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    IMDB_Rating = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Movie, self).save(*args, **kwargs)
    def __str__(self):
        return self.Title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=20, blank=True)
    genres = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.first_name + self.last_name
class Comment(models.Model):
    comment_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    def __str__(self):
        return "{}: Comment {}".format(self.movie_ID, self.comment_ID)



class Rating(models.Model):
    rating_ID = models.AutoField(primary_key=True)
    movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_Rating = models.IntegerField(default=0)

    def __str__(self):
        return "{}: Rating {}".format(self.movie_ID, self.rating_ID)

class WatchedList(models.Model):
    watchedList_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return "Watched list of user {}".format(self.user_ID)