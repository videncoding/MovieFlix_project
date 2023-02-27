from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from movieflix_project.movieflix.models import Movie, UserProfile, Comment, Rating, WatchedList
from movieflix_project.movieflix.serializers import MovieSerializer, UserProfileSerializer, CommentSerializer, RatingSerializer, \
    WatchedListSerializer


# Create your views here.
def movieApi(request, id=0):
    if request.method == 'GET':
        movie = Movie.objects.all()
        movie_serializer = MovieSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie = Movie.objects.get(Movie_ID=movie_data['Movie_ID'])
        movie_serializer = MovieSerializer(movie, data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        movie = Movie.objects.get(Movie_ID=id)
        movie.delete()
        return JsonResponse("Deleted Successfully!", safe=False)


def commentApi(request, id=0):
    if request.method == 'GET':
        comment = Comment.objects.all()
        comment_serializer = CommentSerializer(comment, many=True)
        return JsonResponse(comment_serializer.data, safe=False)
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        comment_data = JSONParser().parse(request)
        comment = Comment.objects.get(Comment_ID=comment_data['Comment_ID'])
        comment_serializer = CommentSerializer(comment, data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        comment = Comment.objects.get(Comment_ID=id)
        comment.delete()
        return JsonResponse("Deleted Successfully!", safe=False)
