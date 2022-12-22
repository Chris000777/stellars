from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    imdbRating = models.FloatField()
    country = models.CharField(max_length=50)
    duration = models.IntegerField()
    # image = models.ImageField(upload_to='profile_pics', default='poster.jpg')
    image = models.CharField(max_length=255, blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    # actors=models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title}"

class Post(models.Model):
    title=models.CharField(max_length=100, verbose_name='Título')
    content=models.TextField(max_length=100, verbose_name='Comentario')
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE,)
    rating = models.IntegerField(blank=True, null=True,)
    alta = models.BooleanField(default=1)

    def soft_delete(self):
        self.alta=False
        super().save()
    
    def restore(self):
        self.alta=True
        super().save()

    def __str__(self):
        return f"{self.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f"{self.user.username} Profile"