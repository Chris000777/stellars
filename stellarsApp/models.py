from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    imdbRating=models.FloatField()
    country=models.CharField(max_length=50)
    duration=models.IntegerField()
    # actors=models.CharField(max_length=250)

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f"{self.user.username} Profile"