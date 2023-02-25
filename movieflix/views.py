from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
#test
def index(request):
    return HttpResponse('Hello')