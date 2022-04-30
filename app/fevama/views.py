from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse

from django.urls import reverse_lazy
from .models import *

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
    return render(request, 'fevama/index.html')

# CHANGE PASSWORD
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('fevama:password_success')

# CHANGE PASSWORD SUCCESS
def password_success(request):
    return render(request, 'fevama/password_success.html')

#### EMPRESAS ####
def projects_index(request):
    return render(request, 'fevama/projects_index.html')

def empresas_index(request):
    object_list = Empresa.objects.all()
    return render(request, 'fevama/empresas_list.html', {
        'object_list': object_list
    })

def contact_index(request):
    object_list = Contact.objects.all()
    return render(request, 'fevama/contact_list.html', {
        'object_list': object_list
    })

def typeofcontact_index(request):
    object_list = TypeOfContact.objects.all()
    return render(request, 'fevama/typeofcontact_list.html', {
        'object_list': object_list
    })

def typeofcontact_create(request):
    return render(request, 'fevama/typeofcontact_create.html')

def typeofcontact_createItem(request):
    type = request.GET['data']
    types = TypeOfContact.objects.all()
    checked = True
    for t in types:
        if type.upper() == t.name.upper():
            checked = False
            response = { 'code': 404 }
        else:
            response = { 'code': 200}
    
    if checked:
        TypeOfContact.objects.create_typeofcontact(type.upper())

    return JsonResponse(response)

def typeofcontact_deleteItem(request):
    id = request.GET['data']
    check = TypeOfContact.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def typeofcontact_modify(request, id):
    contact = TypeOfContact.objects.filter(id=id).first()
    return render(request, 'fevama/typeofcontact_modify.html', {
        'contact': contact
    })

def typeofcontact_modifyItem(request):
    id = request.GET['id']
    type = request.GET['data']

    types = TypeOfContact.objects.all()
    for t in types:
        if type.upper() == t.name.upper():
            response = { 'code': 404 }
            return JsonResponse(response)

    check = TypeOfContact.objects.filter(id=id).first()
    if check:
        check.name = type
        check.save()
    
    response = { 'code': 200}
    return JsonResponse(response)


def economicdata_index(request):
    object_list = EconomicData.objects.all()
    return render(request, 'fevama/economicdata_list.html', {
        'object_list': object_list
    })

def economicdata_create(request):
    empresas_list = Empresa.objects.all()
    return render(request, 'fevama/economicdata_create.html', {
        'empresas_list': empresas_list
    })

def economicdata_createItem(request):
    empresa = request.GET['empresa']
    year = request.GET['year']
    workers = request.GET['workers']
    money = request.GET['money']
    empresa = Empresa.objects.filter(id=empresa).first()
    economic_data = EconomicData.objects.filter(empresa_id=empresa, year=year).first()
    if economic_data:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        EconomicData.objects.create_economicdata(empresa, year, workers, money)
        response = { 'code': 200 }

    return JsonResponse(response)

def economicdata_modify(request, id):
    economic_data = EconomicData.objects.filter(id=id).first()
    empresas_list = Empresa.objects.all()
    return render(request, 'fevama/economicdata_modify.html', {
        'economic_data': economic_data,
        'empresas_list': empresas_list
    })

def economicdata_modifyItem(request):
    id = request.GET['id']
    empresa = request.GET['empresa']
    year = request.GET['year']
    workers = request.GET['workers']
    money = request.GET['money']
    empresa = Empresa.objects.filter(id=empresa).first()

    economic_data = EconomicData.objects.filter(id=id).first()
    if economic_data:
        economic_data.empresa = empresa
        economic_data.year = year
        economic_data.workers = workers
        economic_data.data = money
        economic_data.save()

    response = { 'code' : 200 }
    return JsonResponse(response)

def economicdata_deleteItem(request):
    id = request.GET['data']
    check = EconomicData.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

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
 