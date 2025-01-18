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
from .forms import RegistroUsuarioForm 

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