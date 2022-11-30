from django.shortcuts import render, HttpResponse
from datetime import datetime
from stellarsApp.models import Post, Movie

# -------------- Vistas renderizadas del sitio -------------- #
def home(request):
    return render(request, 'stellarsApp/home.html')

def lounges(request):
    return render(request, 'stellarsApp/lounges.html')

def promotions(request):
    return render(request, 'stellarsApp/promotions.html')

def previews(request,id):
    film=Movie.objects.filter(id=id).first()
    return render(request, 'stellarsApp/previews.html',{'film':film})

def blog(request):
    posts=Post.objects.all()

    return render(request, 'stellarsApp/blog.html', {'posts': posts})

def base(request):
    return render(request, 'stellarsApp/base.html')
