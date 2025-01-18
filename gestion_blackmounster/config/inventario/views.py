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
from .forms import RegistroUsuarioForm, PeliculaForm, UserForm, TransaccionForm
from .models import Transaccion, Pelicula, User

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


@login_required(login_url='/inventario/login/')
def peliculasView(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas.html', {'peliculas': peliculas})

@login_required
def detalle_peliculasView(request, pk):
    peliculas = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'detalle_pelicula.html', {'peliculas': peliculas})

@login_required
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

@login_required
def eliminar_peliculasView(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        pelicula.delete()  
        return redirect('lista_peliculas') 
    return render(request, 'eliminar_pelicula.html', {'pelicula': pelicula})


@login_required
def agregar_peliculasView(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'agregar_pelicula.html', {'form': form})

@login_required
def usuariosView(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

@login_required
def editar_usuariosView(request, pk):
    usuarios = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserForm(instance=usuarios)
    return render(request, 'editar_usuario.html', {'form': form})


@login_required
def eliminar_usuariosView(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        usuario.delete()  
        return redirect('lista_usuarios')  
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})


@login_required
def agregar_usuariosView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserForm()
    return render(request, 'agregar_usuario.html', {'form': form})

@login_required
def arriendo_peliculasView(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.usuario = request.user
            pelicula = prestamo.pelicula
            if pelicula.stock <= 0:
                messages.error(request, f"La película {pelicula.titulo} no tiene stock disponible para arriendo.")
                return redirect('lista_peliculas')
            prestamo.save()
            pelicula.stock -= 1
            pelicula.save()
            messages.success(request, f"Préstamo de la película {pelicula.titulo} creado correctamente.")
            return redirect('lista_peliculas')
    else:
        form = TransaccionForm()
    return render(request, 'arriendo_pelicula.html', {'form': form})

@login_required
def listado_transaccionesView(request):
    if request.user.is_staff:  
        transacciones = Transaccion.objects.all()
    else:
        transacciones = Transaccion.objects.filter(usuario=request.user)
    return render(request, 'transacciones.html', {'transacciones': transacciones})
