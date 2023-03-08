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
def movieApi(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        movie_serializer = MovieSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        filter_movie = Movie.objects.filter(Movie_ID=data['Movie_ID'])
        if not filter_movie.count() ==0:
            return JsonResponse(data, safe=False)
        movie_serializer = MovieSerializer(data=data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(data, safe=False)
        return JsonResponse("Failed to Add.", safe=False)



def commentAddApi(request):
     if request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)


def commentGetApi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_data=Comment.objects.filter(Movie_ID=data['Movie_ID'])
        comment_serializer = CommentSerializer(comment_data, many=True)
        return JsonResponse(comment_serializer.data, safe=False)
def ratingAddApi(request):
    if request.method == 'GET':
        rating = Rating.objects.all()
        rating_serializer = RatingSerializer(rating, many=True)
        return JsonResponse(rating_serializer.data, safe=False)
    elif request.method == 'POST':
        rating_data = JSONParser().parse(request)
        rating_serializer = RatingSerializer(data=rating_data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse("Rating Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

def watchedListApi(request, id=0):
    if request.method == 'GET':
        watchedList = WatchedList.objects.get(User_ID=id)
        movie = watchedList.Movie_ID
        movieList = Movie.objects.get(Movie_ID=movie)
        movie_serializer = MovieSerializer(movieList, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        watchedList_data = Comment.objects.filter(User_ID=data['User_ID'])
        watchedList_serializer = CommentSerializer(watchedList_data, many=True)
        return JsonResponse(watchedList_serializer, safe=False)

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
