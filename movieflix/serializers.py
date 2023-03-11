from rest_framework import serializers
from movieflix.models import Movie, UserProfile, Comment, Rating, WatchedList


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('Movie_ID',
                  'Title',
                  'Poster',
                  'Description',
                  'IMDB_Rating'
                  )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'User_ID',
            'Email',
            'First_name',
            'Last_name',
            'Password',
            'Role',
            'Genres',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('Comment_ID',
                  'User_ID',
                  'Movie_ID',
                  'Comment',
                  )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('Rating_ID',
                  'Movie_ID',
                  'User_ID',
                  'User_Rating',
                  )


class WatchedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchedList
        fields = ('WatchedList_ID',
                  'User_ID',
                  'Movie_ID',
                  )
