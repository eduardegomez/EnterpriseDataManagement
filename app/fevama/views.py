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

# ----------- START EMPRESA ---------------------#
def empresas_index(request):
    object_list = Empresa.objects.all()
    return render(request, 'fevama/empresas_list.html', {
        'object_list': object_list
    })

def empresa_create(request):
    return render(request, 'fevama/empresa_create.html',{})

def empresa_createItem(request):
    name = request.GET['name']
    cif = request.GET['cif']
    cnae = request.GET['cnae']
    phone = request.GET['phone']
    aux = request.GET['aux']
    empresa = Empresa.objects.filter(name=name, cif=cif).first()
    if empresa:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Empresa.objects.create_empresa(name, cif, cnae, phone, aux)
        response = { 'code': 200 }

    return JsonResponse(response)

def empresa_deleteItem(request):
    id = request.GET['data']
    check = Empresa.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def empresa_modify(request, id):
    empresa = Empresa.objects.filter(id=id).first()
    return render(request, 'fevama/empresa_modify.html', {
        'empresa': empresa,
    })

def empresa_modifyItem(request):
    id = request.GET['id']
    name = request.GET['name']
    cif = request.GET['cif']
    cnae = request.GET['cnae']
    phone = request.GET['phone']
    aux = request.GET['aux']
    empresas = Empresa.objects.all()
    for e in empresas:
        if str(e.name) == str(name) and str(e.cif) == str(cif) and str(e.id) != str(id):
            print(e.id)
            print(id)
            response = { 'code': 404 }
            return JsonResponse(response)

    check = Empresa.objects.filter(id=id).first()
    if check:
        check.name = name
        check.cif = cif
        check.cnae = cnae
        check.phone = phone
        check.aux = aux
        check.save()
    
    response = { 'code': 200}
    return JsonResponse(response)
# ----------- END EMPRESA ---------------------#


# ----------- START CONTACT --------------------- #
def contact_index(request):
    object_list = Contact.objects.all()
    return render(request, 'fevama/contact_list.html', {
        'object_list': object_list
    })

def contact_create(request):
    empresas_list = Empresa.objects.all()
    type_list = TypeOfContact.objects.all()
    return render(request, 'fevama/contact_create.html',{
        'empresas_list': empresas_list,
        'type_list': type_list
    })

def contact_createItem(request):
    name = request.GET['name']
    email = request.GET['email']
    empresa = request.GET['empresa']
    type = request.GET['type']
    empresa = Empresa.objects.filter(id=empresa).first()
    type = TypeOfContact.objects.filter(id=type).first()
    contact = Contact.objects.filter(name=name, email=email, empresa=empresa, type=type).first()
    if contact:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Contact.objects.create_contact(name, email, type, empresa)
        response = { 'code': 200 }

    return JsonResponse(response)

def contact_deleteItem(request):
    id = request.GET['data']
    check = Contact.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def contact_modify(request, id):
    contact = Contact.objects.filter(id=id).first()
    empresas_list = Empresa.objects.all()
    type_list = TypeOfContact.objects.all()
    return render(request, 'fevama/contact_modify.html', {
        'contact': contact,
        'empresas_list': empresas_list,
        'type_list': type_list
    })

def contact_modifyItem(request):
    id = request.GET['id']
    name = request.GET['name']
    email = request.GET['email']
    empresa = request.GET['empresa']
    type = request.GET['type']
    empresa = Empresa.objects.filter(id=empresa).first()
    type = TypeOfContact.objects.filter(id=type).first()
    contacts = Contact.objects.all()
    for c in contacts:
        if c.name == name and c.email == email and c.empresa == empresa and c.type == type and str(c.id) != str(id):
            response = { 'code': 404 }
            return JsonResponse(response)

    check = Contact.objects.filter(id=id).first()
    if check:
        check.name = name
        check.email = email
        check.empresa = empresa
        check.type = type
        check.save()
    
    response = { 'code': 200}
    return JsonResponse(response)

# ----------- END CONTACT --------------------- #


# ----------- START TYPE OF CONTACT --------------------- #
def typeofcontact_index(request):
    lenght = len(TypeOfContact.objects.all())
    object_list = TypeOfContact.objects.all()[:20]
    return render(request, 'fevama/typeofcontact_list.html', {
        'object_list': object_list,
        'lenght': lenght
    })

def typeofcontact_showAll(request):
    object_list = TypeOfContact.objects.all()[20:]
    data = []

    for o in object_list:
        data_aux = dict()
        data_aux["id"] = o.id
        data_aux["type"] = o.name
        data.append(data_aux)

    response = { 'code': 200, 'data': data}
    return JsonResponse(response)

def typeofcontact_create(request):
    return render(request, 'fevama/typeofcontact_create.html')

def typeofcontact_createItem(request):
    type = request.GET['data']
    types = TypeOfContact.objects.all()

    for t in types:
        if type.upper() == t.name.upper():
            response = { 'code': 404 }
            return JsonResponse(response)
        
    TypeOfContact.objects.create_typeofcontact(type.upper())
    response = { 'code': 200}
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

# ----------- END TYPE OF CONTACT --------------------- #


# ----------- START ECONOMIC DATA --------------------- #
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

# ----------- END ECONOMIC DATA --------------------- #


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
 