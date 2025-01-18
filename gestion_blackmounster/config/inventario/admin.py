from django.contrib import admin
from .models import User, Pelicula, Transaccion
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

# Register your models here.

class CustomUserCreationForm(UserAdmin):
    add_form = CustomUserCreationForm
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "password1", "password2"),
        }),
    )
    
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    
admin.site.unregister(User)
admin.site.register(User, CustomUserCreationForm)
    
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'genero', 'precio_compra', 'precio_arriendo', 'stock')
    search_fields = ('titulo', 'director', 'genero')
    list_filter = ('titulo', 'stock')
    ordering = ('id', 'titulo')
    
@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pelicula', 'tipo', 'fecha_inicio', 'fecha_termino', 'estado')
    search_fields = ('usuario', 'pelicula', 'estado')
    list_filter = ('usuario', 'pelicula')
    ordering = ('usuario', 'pelicula')
    
