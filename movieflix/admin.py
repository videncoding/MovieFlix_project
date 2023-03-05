from django.contrib import admin
from movieflix.models import Movie, UserProfile, Comment, WatchedList, Rating
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Title',)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(WatchedList)
admin.site.register(Rating)