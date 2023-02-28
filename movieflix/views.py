from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from movieflix_project.movieflix.models import Movie, UserProfile, Comment, Rating, WatchedList
from movieflix_project.movieflix.serializers import MovieSerializer, UserProfileSerializer, CommentSerializer, \
    RatingSerializer, \
    WatchedListSerializer
from django.core.files.storage import default_storage


# Create your views here.
def movieApi(request, id=0):
    if request.method == 'GET':
        movie = Movie.objects.all()
        movie_serializer = MovieSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        movie = Movie.objects.get(Movie_ID=id)
        if movie.is_valid():
            movie_serializer = MovieSerializer(movie, many=True)
            return JsonResponse(movie_serializer.data, safe=False)
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
        comment = Comment.Comment.has_default(Movie_ID=id)
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


def ratingApi(request, id=0):
    if request.method == 'GET':
        rating = Rating.User_Rating.get(Movie_ID=id)
        rating_serializer = RatingSerializer(rating, many=True)
        return JsonResponse(rating_serializer.data, safe=False)
    elif request.method == 'POST':
        rating_data = JSONParser().parse(request)
        rating_serializer = RatingSerializer(data=rating_data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        rating_data = JSONParser().parse(request)
        rating = Rating.objects.get(Rating_ID=rating_data['Rating_ID'])
        rating_serializer = RatingSerializer(rating, data=rating_data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        rating = Rating.objects.get(Rating_ID=id)
        rating.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

def watchedListApi(request, id=0):
    if request.method == 'GET':
        watchedList = WatchedList.objects.get(User_ID=id)
        movie = watchedList.Movie_ID
        movieList = Movie.objects.get(Movie_ID=movie)
        movie_serializer = MovieSerializer(movieList, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        watchList_data = JSONParser().parse(request)
        watchList_serializer = WatchedListSerializer(data=watchList_data)
        if watchList_serializer.is_valid():
            watchList_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        watchedList_data = JSONParser().parse(request)
        watchedList = WatchedList.objects.get(WatchedLIST_ID=watchedList_data['WatchedList_ID'])
        watchedList_serializer = WatchedListSerializer(watchedList, data=watchedList_data)
        if watchedList_serializer.is_valid():
            watchedList_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        watchedList = WatchedList.objects.get(Movie_ID=id)
        watchedList.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
