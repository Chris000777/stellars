from django.shortcuts import render, HttpResponse, redirect
from stellarsApp.forms import PostForm, ContactoForm, RegistrarUsuarioForm
from datetime import datetime
from stellarsApp.models import Post, Movie
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required

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

@login_required(login_url='/account/login/')
@permission_required('stellarsApp.view_post', login_url='/')
def base_admin(request):
    return render(request, 'stellarsAdmin/base_admin.html')

@login_required(login_url='/account/login/')
@permission_required('stellarsApp.view_post', login_url='/')
def post(request):
    #query set
    posts = Post.objects.all()
    return render(request,'stellarsAdmin/post/index.html',{'posts': posts})

@login_required(login_url='/account/login/')
@permission_required('stellarsApp.add_post', login_url='/')
def post_nuevo(request):
    if(request.method=='POST'):
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Posts')
    else:
        formulario = PostForm()
    return render(request,'stellarsAdmin/post/new.html',{'formulario':formulario})

@login_required(login_url='/account/login/')
@permission_required('stellarsApp.view_post', login_url='/')
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

@login_required(login_url='/account/login/')
@permission_required('stellarsApp.view_post', login_url='/')
def post_eliminar(request,id_post):
    try:
        post = Post.objects.get(pk=id_post)
    except Post.DoesNotExist:
        return render(request,'stellarsAdmin/404_admin.html')
    post.delete()
    return redirect('Posts')

def stellars_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get('next',None)
            if nxt is None:
                return redirect('Inicio')
            else:
                return redirect(nxt)
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'stellarsAdmin/registration/login.html', {'form': form})

def stellars_registro(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()        
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'stellarsAdmin/registration/registrarse.html', {'form': form})