from movieflix_project.movieflix import views
from django.urls import path

urlpatterns = [
    path('movie/', views.movieApi),
    path('movie/([0-9]+)', views.movieApi()),
    path('comment/', views.commentApi),
    path('comment/([0-9]+)', views.commentApi())
]
