from movieflix import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('movie/movieGet', csrf_exempt(views.movieGetApi)),
                  path('movie/movieSearch', csrf_exempt(views.movieSearchApi)),
                  path('comment/commentAdd', csrf_exempt(views.commentAddApi)),
                  path('comment/commentGet', csrf_exempt(views.commentGetApi)),
                  path('comment/commentDel', csrf_exempt(views.commentDel)),
                  path('movie/SaveFile', views.SaveFile),
                  path('rating/ratingAdd', csrf_exempt(views.ratingAddApi)),
                  path('watchedList/watchedListAdd', csrf_exempt(views.watchedListAddApi)),
                  path('watchedList/watchedListSearch', csrf_exempt(views.watchedListSearchApi)),
                  path('userprofile/', csrf_exempt(views.userprofileRegisterApi)),
                  path('userprofile/register', csrf_exempt(views.userprofileRegisterApi)),
                  path('userprofile/login', csrf_exempt(views.userprofileLoginApi)),
                  path('userprofile/get', csrf_exempt(views.userprofileGetApi)),
                  path('userprofile/put', csrf_exempt(views.userprofilePutApi)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
