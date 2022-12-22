from django.contrib import admin
from stellarsApp.models import Post, Movie, Profile
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','alta']
    list_filter = ('author',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(Profile)