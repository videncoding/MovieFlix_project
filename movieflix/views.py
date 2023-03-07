from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from movieflix.models import Movie, UserProfile, Comment, Rating, WatchedList
from movieflix.serializers import MovieSerializer, UserProfileSerializer, CommentSerializer, \
    RatingSerializer, \
    WatchedListSerializer
from django.core.files.storage import default_storage


from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
import json
from django.contrib.auth.decorators import login_required

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
            movie_serializer1 = MovieSerializer(movie, many=True)
            return JsonResponse(movie_serializer1, safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    # elif request.method == 'PUT':
    #     movie_data = JSONParser().parse(request)
    #     movie = Movie.objects.get(Movie_ID=movie_data['Movie_ID'])
    #     movie_serializer = MovieSerializer(movie, data=movie_data)
    #     if movie_serializer.is_valid():
    #         movie_serializer.save()
    #         return JsonResponse("Updated Successfully", safe=False)
    #     return JsonResponse("Failed to Update", safe=False)
    # elif request.method == 'DELETE':
    #     movie = Movie.objects.get(Movie_ID=id)
    #     movie.delete()
    #     return JsonResponse("Deleted Successfully!", safe=False)


def commentApi(request, id=0):
    if request.method == 'GET':
        comment = Comment.objects.get(Movie_ID=id)
        comment_serializer = CommentSerializer(comment.Comment, many=True)
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
        rating = Rating.objects.get(Movie_ID=id)
        rating_serializer = RatingSerializer(rating.User_Rating, many=True)
        return JsonResponse(rating_serializer.data, safe=False)
    elif request.method == 'POST':
        rating_data = JSONParser().parse(request)
        rating_serializer = RatingSerializer(data=rating_data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse("Rating Successfully!", safe=False)
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
def userprofileApi(request):
    if request.method == 'GET':
        userprofile = UserProfile.objects.all()
        userprofile_serializer = UserProfileSerializer(userprofile, many=True)
        return JsonResponse(userprofile_serializer.data, safe=False)
    elif request.method == 'POST':
        userprofile_data = JSONParser().parse(request)
        userprofile_serializer = UserProfileSerializer(data=userprofile_data)
        if userprofile_serializer.is_valid():
            userprofile_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    # elif request.method == 'DELETE':
    #     id=request.get('User_ID')
    #     userprofile_serializer = UserProfileSerializer(data=id)
    #     userprofile = UserProfile.objects.get(User_ID=userprofile_serializer)
    #     userprofile.delete()
    #     return JsonResponse("Deleted Successfully!", safe=False)

def userprofileLoginApi(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            filter_user = UserProfile.objects.filter(Username=data['Username'])
            if not len(filter_user):
                res = {
                    'success': False,
                    'mess': 'Username not registered'
                }
                return JsonResponse(res, safe=False)
            User_data = UserProfile.objects.get(Username=data['Username'])

            if not data['Password']==User_data.Password:
                res = {
                    'success': False,
                    'mess': 'Password error'
                }
                return JsonResponse(res, safe=False)

            res = {
                'success': True,
                'User_ID':User_data.User_ID,
                'mess': 'Login Successfully'
            }
            return JsonResponse(res, safe=False)







def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
