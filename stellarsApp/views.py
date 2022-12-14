from django.shortcuts import render, HttpResponse
from stellarsApp.forms import ContactoForm
from datetime import datetime
from stellarsApp.models import Post, Movie

# -------------- Vistas renderizadas del sitio -------------- #
def home(request):
    mensaje=None
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)
        if (contacto_form.is_valid()):
            mensaje='Gracias por su compra. En minutos recibirá un mail con su ticket virtual'
        else:
            mensaje='Error'
    else:
        contacto_form = ContactoForm()
    return render(request, 'stellarsApp/home.html',{'contacto_form':contacto_form, 'mensaje':mensaje})

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
