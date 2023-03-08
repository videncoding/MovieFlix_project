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
def movieGetApi(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        movie_serializer = MovieSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        filter_movie = Movie.objects.filter(Movie_ID=data['Movie_ID'])
        if not filter_movie.count() == 0:
            return JsonResponse(data, safe=False)
        movie_serializer = MovieSerializer(data=data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(data, safe=False)
        return JsonResponse("Failed to Add.", safe=False)

def movieSearchApi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        movie_data = Movie.objects.filter(Movie_ID=data['Movie_ID'])
        movie_serializer = MovieSerializer(movie_data, many=True)
        return JsonResponse(movie_serializer.data, safe=False)


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
        comment_data = Comment.objects.filter(Movie_ID=data['Movie_ID'])
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


def watchedListSearchApi(request):
    if request.method == 'GET':
        watchedList = WatchedList.objects.all()
        watchedList_serializer = WatchedListSerializer(watchedList, many=True)
        return JsonResponse(watchedList_serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        watched_data = WatchedList.objects.filter(User_ID=data['User_ID'])
        watched_serializer = WatchedListSerializer(watched_data, many=True)
        return JsonResponse(watched_serializer.data, safe=False)


def watchedListAddApi(request):
    if request.method == 'POST':
        watchedList_data = JSONParser().parse(request)
        watchedList_serializer = WatchedListSerializer(data=watchedList_data)
        if watchedList_serializer.is_valid():
            watchedList_serializer.save()
            return JsonResponse("WatchedList added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)


def userprofileRegisterApi(request):
    if request.method == 'GET':
        userprofile = UserProfile.objects.all()
        userprofile_serializer = UserProfileSerializer(userprofile, many=True)
        return JsonResponse(userprofile_serializer.data, safe=False)
    elif request.method == 'POST':
        userprofile_data = JSONParser().parse(request)
        userprofile_serializer = UserProfileSerializer(data=userprofile_data)
        if userprofile_serializer.is_valid():
            userprofile_serializer.save()
            if userprofile_data['Email'] == "admin@admin.com" and userprofile_data['Password'] == "admin":
                user_admin=UserProfile.objects.get(Username=userprofile_data['Username'])
                user_admin.is_staff=True
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

def userprofileGetApi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userprofile_data = UserProfile.objects.filter(User_ID=data['User_ID'])
        userprofile_serializer = UserProfileSerializer(userprofile_data, many=True)
        return JsonResponse(userprofile_serializer.data, safe=False)

def userprofilePutApi(request):
    if request.method == 'PUT':
        userprofile_data = JSONParser().parse(request)
        useeprofile=UserProfile.objects.get(User_ID=userprofile_data['User_ID'])
        userprofile_serializer = UserProfileSerializer(useeprofile, data=userprofile_data)
        if userprofile_serializer.is_valid():
            userprofile_serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to Update.",safe=False)


def userprofileLoginApi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        filter_user = UserProfile.objects.filter(Email=data['Email'])
        if not len(filter_user):
            res = {
                'success': False,
                'mess': 'Email not registered'
            }
            return JsonResponse(res, safe=False)
        User_data = UserProfile.objects.get(Email=data['Email'])

        if not data['Password'] == User_data.Password:
            res = {
                'success': False,
                'mess': 'Password error'
            }
            return JsonResponse(res, safe=False)

        res = {
            'success': True,
            'User_ID': User_data.User_ID,
            'isStaff': User_data.is_staff,
            'Genres':User_data.Genres,
            'mess': 'Login Successfully'
        }
        return JsonResponse(res, safe=False)


def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
