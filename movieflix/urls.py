from movieflix_project.movieflix import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('movie', views.movieApi),
                  path('movie/([0-9]+)', views.movieApi),
                  path('comment', views.commentApi),
                  path('comment/([0-9]+)', views.commentApi),
                  path('Movie/SaveFile', views.SaveFile),
                  path('rating', views.ratingApi),
                  path('rating/([0-9]+)', views.ratingApi),
                  path('watchedList', views.watchedListApi),
                  path('watchedList/([0-9]+)', views.watchedListApi),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
