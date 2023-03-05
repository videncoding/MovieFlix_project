from django.urls import path
from movieflix import views

app_name = 'movieflix'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('profile/mycomments/userid', views.mycomments, name='mycomments'),
    path('<slug:movie_title_slug>/', views.detail, name='detail')
]

