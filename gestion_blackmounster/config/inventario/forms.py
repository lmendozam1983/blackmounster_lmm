from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Pelicula, Transaccion

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Este correo electrónico ya está en uso.")
            return email
        

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Contraseña")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Nombre de usuario o contraseña incorrectos.")
        return cleaned_data


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        
class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__'