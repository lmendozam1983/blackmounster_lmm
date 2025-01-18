from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registroView, name='register'),
    path('peliculas/', views.peliculasView, name='lista_peliculas'),
    path('detalle_pelicula/<int:pk>', views.detalle_peliculasView, name='detalle_pelicula'),
    path('editar_pelicula/<int:pk>', views.editar_peliculasView, name='editar_pelicula'),
    path('eliminar_pelicula/<int:pk>', views.eliminar_peliculasView, name='eliminar_pelicula'),
    path('agregar_pelicula/', views.agregar_peliculasView, name='agregar_pelicula'),
]