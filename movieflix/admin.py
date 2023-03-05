from django.contrib import admin
from movieflix.models import Movie, UserProfile, Comment, WatchedList, Rating
# Register your models here.

admin.site.register(Movie)
# 注册userProfile模型
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(WatchedList)
admin.site.register(Rating)