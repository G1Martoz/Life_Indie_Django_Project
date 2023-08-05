# from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.


class LoginUsuario(LoginView):
    template_name = 'registrar/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Se inició sesión correctamente')

        return reverse('home')


class LogoutUsuario(LogoutView):
    template_name = 'registrar/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Se cerro exitosamente la sesión')

        return reverse('apps.usuario:logout')


class RegistrarUsuario(CreateView):
    template_name = 'registrar/RegistrarUsuario.html'
    form_class = RegistroUsuarioForm

    def from_valid(self, form):
        messages.success(
            self.request, 'Registro exitoso. Por favor, inicie sesión.')
        form.save()

        return redirect('apps.usuario:RegistrarUsuario')
