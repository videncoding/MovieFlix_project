from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
from movieflix.models import Movie

def index(request):
    return HttpResponse('Hello')

# Returns personal detail page
def profile(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

def watchlist(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

def mycomments(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

def detail(request):
    context_dict = {}
    if request.method == 'POST':
        Movie_ID = request.POST['Movie_ID']
        Title = request.POST['Title']

    return HttpResponse("Hi there")

def register(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

def login(request):
    context_dict = {}
    return render(request, 'profile.html', context=context_dict)

# Returns to the front page when loging out
def logout(request):
    return render(request, '<index file>')