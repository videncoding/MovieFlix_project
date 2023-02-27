from movieflix_project.movieflix import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('movie/', views.movieApi),
    path('movie/([0-9]+)', views.movieApi()),
    path('comment/', views.commentApi),
    path('comment/([0-9]+)', views.commentApi()),
    path('Movie/SaveFile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
