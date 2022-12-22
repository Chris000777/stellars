from django.shortcuts import render, HttpResponse, redirect
from stellarsApp.forms import PostForm, ContactoForm
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
    posts=Post.objects.filter(alta=True)
    return render(request, 'stellarsApp/blog.html', {'posts': posts})

def base(request):
    return render(request, 'stellarsApp/base.html')

def base_admin(request):
    return render(request, 'stellarsAdmin/base_admin.html')

def post(request):
    #query set
    posts = Post.objects.all()
    return render(request,'stellarsAdmin/post/index.html',{'posts': posts})

def post_nuevo(request):
    if(request.method=='POST'):
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Posts')
    else:
        formulario = PostForm()
    return render(request,'stellarsAdmin/post/new.html',{'formulario':formulario})

def post_editar(request,id_post):
    try:
        post = Post.objects.get(pk=id_post)
    except Post.DoesNotExist:
        return render(request,'stellarsAdmin/404_admin.html')
    if(request.method == 'POST'):
        formulario = PostForm(request.POST,instance=post)
        if formulario.is_valid():
            formulario.save()
            return redirect('Posts')
    else:
       formulario = PostForm(instance=post)
    return render(request,'stellarsAdmin/post/edit.html',{'formulario':formulario})

def post_eliminar(request,id_post):
    try:
        post = Post.objects.get(pk=id_post)
    except Post.DoesNotExist:
        return render(request,'stellarsAdmin/404_admin.html')
        confirm('Desea eliminar este comentario')
    post.delete()
    return redirect('Posts')
