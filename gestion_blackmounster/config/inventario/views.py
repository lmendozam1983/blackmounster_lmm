# Django
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect#
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate
from django.contrib import messages 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test


# 
from .forms import RegistroUsuarioForm, PeliculaForm
from .models import Transaccion, Pelicula

# Create your views here.

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                next_url = '/index/'
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})

def logoutView(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 

def registroView(request): 
    if request.method == "POST": 
        form = RegistroUsuarioForm(request.POST) 
        if form.is_valid(): 
            content_type = ContentType.objects.get_for_model(Transaccion) 
            visualizar_listado = Permission.objects.get(
                codename='visualizar_listado', 
                content_type=content_type
            ) 
            user = form.save() 
            user.user_permissions.add(visualizar_listado) 
            login(request, user)
            next_url = '/'
            messages.success(request, "Registrado satisfactoriamente.") 
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Registro inválido. Algunos datos son incorrectos.") 
    else:
        form = RegistroUsuarioForm()  
    
    return render(request, 'register.html', {'register_form': form})

def peliculasView(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas.html', {'peliculas': peliculas})

def detalle_peliculasView(request, pk):
    peliculas = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'detalle_pelicula.html', {'peliculas': peliculas})

def editar_peliculasView(request, pk):
    peliculas = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=peliculas)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm(instance=peliculas)
    return render(request, 'editar_pelicula.html', {'form': form})

def eliminar_peliculasView(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'eliminar_pelicula.html', {'pelicula': pelicula})

def agregar_peliculasView(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'agregar_pelicula.html', {'form': form})

