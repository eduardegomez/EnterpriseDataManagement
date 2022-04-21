from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

# Create your views here. 
  
# LOGIN                       
def login_view(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  
        return redirect('/fevama/home') 
    else:
        return render(request, 'admin/login.html', {
            'code': 404,
        })

# LOGOUT
def logout_view(request):

    logout(request)
    return redirect('/admin/app/login/')

# HOME  
def home(request):

    return render(request, 'fevama/index.html', {})

# CHANGE PASSWORD
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('fevama:password_success')

# CHANGE PASSWORD SUCCESS
def password_success(request):
    return render(request, 'fevama/password_success.html')

#### PROYECTOS ####
def projects_index(request):
    return render(request, 'fevama/projects_index.html')

#### AYUDAS ####
def ayudas_index(request):
    return render(request, 'fevama/ayudas_index.html')

#### PLANIFICACIÓN ####
def planificacion_index(request):
    return render(request, 'fevama/planificacion_index.html')

#### NOTIFICACIONES ####
def notificaciones_index(request):
    return render(request, 'fevama/notificaciones_index.html')

#### BASE DE DATOS ####
def bd_index(request):
    return render(request, 'fevama/bd_index.html')

#### PARAMETROS ####
def parametros_index(request):
    return render(request, 'fevama/parametros_index.html')
 