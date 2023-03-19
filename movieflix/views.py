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
            movie = Movie.objects.get(Movie_ID=data['Movie_ID'])
            res = {
                "Movie_ID": movie.Movie_ID,
                "Title": movie.Title,
                "Poster": movie.Poster,
                "Description": movie.Description,
                "IMDB_Rating": movie.IMDB_Rating,
                "User_Rating": movie.Average_Rating
            }
            return JsonResponse(res, safe=False)
        movie_serializer = MovieSerializer(data=data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            movie=Movie.objects.get(Movie_ID=data['Movie_ID'])
            res= {
                "Movie_ID": movie.Movie_ID,
                "Title": movie.Title,
                "Poster": movie.Poster,
                "Description": movie.Description,
                "IMDB_Rating": movie.IMDB_Rating,
                "User_Rating": movie.Average_Rating
            }
            return JsonResponse(res, safe=False)
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
        for comment in comment_serializer.data:
            user_object = UserProfile.objects.filter(User_ID=comment['User_ID'])[0]
            first_name = user_object.First_Name
            last_name = user_object.Last_Name
            comment['First_Name'] = first_name
            comment['Last_Name'] = last_name
        return JsonResponse(comment_serializer.data, safe=False)

def commentDel(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_data = Comment.objects.filter(Comment_ID=data['Comment_ID'])
        comment_data.delete()
        res = {"msg": "Delete successful",
               "status_code": 200}
        return JsonResponse(res, safe=False)
    res = {
        "msg": "Failed Delete!",
        "status_code": 500
    }
    return JsonResponse(res, safe=False)



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
            all_ratings = Rating.objects.filter(Movie_ID=rating_data['Movie_ID'])
            sum=0
            cnt=0
            for rate in all_ratings:
                sum += rate.User_Rating
                cnt += 1
            movie=Movie.objects.get(Movie_ID=rating_data['Movie_ID'])
            movie.Average_Rating=sum / cnt
            movie.save()
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
        # print(watched_data)
        # watched_serializer = WatchedListSerializer(watched_data, many=True)
        res = {"User_id":data["User_ID"]}
        for Watched in watched_data:
            # print(Watched.Movie_ID.Movie_ID)
            movie=Movie.objects.get(Movie_ID=Watched.Movie_ID.Movie_ID)
            # print(movie.Title)
            res[f"{movie.Movie_ID}"] = {
                "Movie_ID": movie.Movie_ID,
                "Title": movie.Title,
                "Poster": movie.Poster,
                "Description": movie.Description,
                "IMDB_Rating": movie.IMDB_Rating,
                "User_Rating": movie.Average_Rating
            }
        return JsonResponse(res, safe=False)



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
        print(userprofile_data)
        print(userprofile_serializer.is_valid())
        print(userprofile_serializer)
        if userprofile_serializer.is_valid():
            userprofile_serializer.save()
            if userprofile_data['Email'] == "admin@admin.com" and userprofile_data['Password'] == "admin":
                user_admin = UserProfile.objects.get(Email=userprofile_data['Email'])
                user_admin.Is_Staff = True
                user_admin.save()
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
            'Email': User_data.Email,
            'isStaff': User_data.Is_Staff,
            'Genres': User_data.Genres,
            'First_Name': User_data.First_Name,
            'Last_Name': User_data.Last_Name,
            'mess': 'Login Successfully'
        }
        return JsonResponse(res, safe=False)


def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
