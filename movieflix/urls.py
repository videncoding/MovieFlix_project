from movieflix import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('movie/', csrf_exempt(views.movieApi)),
                  path(r'^movie/([0-9]+)$', views.movieApi),
                  path('comment/commentAdd', csrf_exempt(views.commentAddApi)),
                  path('comment/([0-9]+)', views.commentAddApi),
                  path('comment/commentGet', csrf_exempt(views.commentGetApi)),
                  path('movie/SaveFile', views.SaveFile),
                  path('rating/ratingAdd', csrf_exempt(views.ratingAddApi)),
                  path('rating/([0-9]+)', views.ratingAddApi),
                  path('watchedList/', views.watchedListApi),
                  path('watchedList/([0-9]+)', views.watchedListApi),
                  path('userprofile/', csrf_exempt(views.userprofileApi)),
                  path('userprofile/register', csrf_exempt(views.userprofileApi)),
                  path('userprofile/login', csrf_exempt(views.userprofileLoginApi)),
                  path(r'userprofile/([0-9]+)$', csrf_exempt(views.userprofileApi)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
