from django.urls import path
from movieflix import views

app_name = 'movieflix'

urlpatterns = [
    path('', views.index, name='index'),

]

