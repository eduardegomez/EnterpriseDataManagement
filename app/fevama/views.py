from ast import Or
import datetime
import mimetypes
from sre_constants import SUCCESS
from typing import final
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse, HttpResponse
import json

from django.urls import reverse_lazy
from .models import *
import os
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect

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

# ----------- EMPRESA GRAPHS ------------------------ #
def graphs_index(request):
    object_list = Empresa.objects.all()
    return render(request, 'fevama/graphs_index.html', {
        'object_list': object_list
    })

def empresa_getdatagraph(request):
    data = dict()
    final_data = {}
    year = []
    value = []
    workers = []
    id = request.GET["identifier"]
    start = request.GET["start"]
    end = request.GET["end"]

    if start == "" or end == "":
        response = { 'code': 404 }
        return JsonResponse(response)
    elif start > end:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        start = int(start)
        end = int(end)

    all_data = EconomicData.objects.filter(empresa_id=id).filter(year__range=[start,end]).order_by('year')
    if all_data:
        for d in all_data:
            year.append(d.year)
            value.append(d.data)
            workers.append(d.workers)

    final_data['chart_data'] = [{'year': year}, {'value': value}, {'workers': workers}]
    data = final_data
    return HttpResponse(json.dumps(data), content_type='aplication/json')

def empresa_compare(request):
    data = dict()
    id1 = request.GET["identifier1"]
    id2 = request.GET["identifier2"]
    start = request.GET["start"]
    end = request.GET["end"]

    if start == "" or end == "":
        response = { 'code': 404 }
        return JsonResponse(response)
    elif start > end:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        start = int(start)
        end = int(end)

    year = []
    start_aux = start
    while start_aux <= end:
        year.append(start_aux)
        start_aux += 1

    year1 = []
    value1 = []
    workers1 = []
    empresa = Empresa.objects.filter(id=id1).first()
    name1 = empresa.name
    all_data1 = EconomicData.objects.filter(empresa_id=id1).filter(year__range=[start,end]).order_by('year')
    start1 = start
    if all_data1:
        for d in all_data1:
            while d.year != start1:
                year1.append(start1)
                value1.append(0)
                workers1.append(0)
                start1 += 1

            year1.append(d.year)
            value1.append(d.data)
            workers1.append(d.workers)
            start1 += 1

    year2 = []
    value2 = []
    workers2 = []
    empresa = Empresa.objects.filter(id=id2).first()
    name2 = empresa.name
    all_data2 = EconomicData.objects.filter(empresa_id=id2).filter(year__range=[start,end]).order_by('year')
    start2 = start
    if all_data2:
        for d in all_data2:
            while d.year != start2:
                year2.append(start2)
                value2.append(0)
                workers2.append(0)
                start2 += 1

            year2.append(d.year)
            value2.append(d.data)
            workers2.append(d.workers)
            start2 += 1

    data = dict()
    data["first"] = [{'year': year1}, {'value': value1}, {'workers': workers1}, {'name': name1}]
    data["second"] = [{'year': year2}, {'value': value2}, {'workers': workers2}, {'name': name2}]

    return HttpResponse(json.dumps(data), content_type='aplication/json')


# ----------- END GRAPHS----------------------------- #

#### SUBVENCIONES ####
def ayudas_index(request):
    return render(request, 'fevama/ayudas_index.html')

# ----------- START PROJECTS ----------------------------- #
def project_index(request):
    object_list = Project.objects.all()
    return render(request, 'fevama/project_list.html', {
        'object_list' : object_list
    })

def project_create(request):
    empresas_list = Empresa.objects.all()
    invoice_list = Invoice.objects.all()
    assistance_list = Assistance.objects.all()
    return render(request, 'fevama/project_create.html', {
        'empresas_list': empresas_list,
        'invoice_list': invoice_list,
        'assistance_list': assistance_list
    })

def project_createItem(request):
    assistance = request.GET['assistance']
    empresa = request.GET['empresa']
    invoice = request.GET['invoice']
    
    check = Project.objects.filter(assistance_id=assistance, empresa_id=empresa, invoice_id=invoice).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        empresa = Empresa.objects.filter(id=empresa).first()
        assistance = Assistance.objects.filter(id=assistance).first()
        invoice = Invoice.objects.filter(id=invoice).first()
        Project.objects.create_project(empresa, assistance, invoice)
    
    response = { 'code': 200}
    return JsonResponse(response)

def project_deleteItem(request):
    id = request.GET['data']
    check = Project.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def project_modify(request, id):
    project = Project.objects.filter(id=id).first()
    empresas_list = Empresa.objects.all()
    invoice_list = Invoice.objects.all()
    assistance_list = Assistance.objects.all()
    return render(request, 'fevama/project_modify.html', {
        'project': project,
        'empresas_list': empresas_list,
        'invoice_list': invoice_list,
        'assistance_list': assistance_list
    })

def project_modifyItem(request):
    id = request.GET['id']
    assistance = request.GET['assistance']
    invoice = request.GET['invoice']
    empresa = request.GET['empresa']
    empresa = Empresa.objects.filter(id=empresa).first()
    invoice = Invoice.objects.filter(id=invoice).first()
    assistance = Assistance.objects.filter(id=assistance).first()
    projects = Project.objects.all()
    for p in projects:
        if p.assistance == assistance and p.empresa == empresa and p.invoice == invoice:
            response = { 'code': 404 }
            return JsonResponse(response)

    check = Project.objects.filter(id=id).first()
    if check:
        check.assistance = assistance
        check.invoice = invoice
        check.empresa = empresa
        check.save()
    
    response = { 'code': 200}
    return JsonResponse(response)
# ----------- END PROJECTS ----------------------------- #

# ----------- START INVOICE ----------------------------- #
def invoice_index(request):
    object_list = Invoice.objects.all()
    return render(request, 'fevama/invoice_list.html', {
        'object_list': object_list
    })

def invoice_create(request):
    return render(request, 'fevama/invoice_create.html', {
    })

def invoice_deleteItem(request):
    id = request.GET['data']
    check = Invoice.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def invoice_createItem(request):
    number = request.GET['number']
    invoice = request.GET['invoice']
    year = request.GET['year']
    amount = request.GET['amount']
    date = request.GET['date']
    
    check = Invoice.objects.filter(number=number).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Invoice.objects.create_invoice(number, invoice, year, amount, date)
    
    response = { 'code': 200}
    return JsonResponse(response)

def invoice_modify(request, id):
    invoice = Invoice.objects.filter(id=id).first()
    return render(request, 'fevama/invoice_modify.html', {
        'invoice': invoice
    })

def invoice_modifyItem(request):
    number = request.GET['number']
    invoice = request.GET['invoice']
    year = request.GET['year']
    amount = request.GET['amount']
    date = request.GET['date']
    id = request.GET['id']
    invoices = Invoice.objects.all()
    for i in invoices:
        if str(i.number) == str(invoice):
            response = { 'code': 404 }
            return JsonResponse(response)
    
    check = Invoice.objects.filter(id=id).first()
    if check:
        check.number = number
        check.invoice = invoice
        check.year = year
        check.amount = amount
        check.date = date
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)

# ----------- END INVOICE ----------------------------- #

# ----------- START ASSISTANCE ----------------------------- #
def assistance_index(request):
    object_list = Assistance.objects.all()
    return render(request, 'fevama/assistance_list.html', {
        'object_list': object_list
    })

def assistance_details(request, id):
    assistance = Assistance.objects.filter(id=id).first()
    return render(request, 'fevama/assistance_details.html', {
        'assistance': assistance
    })

def assistance_deleteItem(request):
    id = request.GET['data']
    check = Assistance.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def assistance_create(request):
    line_list = Line.objects.all()
    act_list = Act.objects.all()
    organism_list = Organism.objects.all()
    situation_list = Situation.objects.all()
    applicant_list = Applicant.objects.all()
    announcement_list = Announcement.objects.all()
    return render(request, 'fevama/assistance_create.html', {
        'line_list': line_list,
        'act_list': act_list,
        'organism_list': organism_list,
        'situation_list': situation_list,
        'applicant_list': applicant_list,
        'announcement_list': announcement_list
    })

def assistance_createItem(request):
    line = request.GET['line']
    line = Line.objects.filter(id=line).first()
    act = request.GET['act']
    act = Act.objects.filter(id=act).first()
    organism = request.GET['organism']
    organism = Organism.objects.filter(id=organism).first()
    situation = request.GET['situation']
    situation = Situation.objects.filter(id=situation).first()
    applicant = request.GET['applicant']
    applicant = Applicant.objects.filter(id=applicant).first()
    announcement = request.GET['announcement']
    announcement = Announcement.objects.filter(id=announcement).first()
    management = request.GET['management']
    requested = request.GET['requested']
    applied = request.GET['applied']
    date = request.GET['date']
    payment = request.GET['payment']
    check = Assistance.objects.filter(line=line, act=act, organism=organism, situation=situation, applicant=applicant, management=management, requested=requested, applied=applied, date=date, payment=payment).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Assistance.objects.create_assistance(line, act, organism, announcement, situation, applicant, management, requested, applied, date, payment)
    
    response = { 'code': 200}
    return JsonResponse(response)

def assistance_modify(request, id):
    assistance = Assistance.objects.filter(id=id).first()
    line_list = Line.objects.all()
    act_list = Act.objects.all()
    organism_list = Organism.objects.all()
    situation_list = Situation.objects.all()
    applicant_list = Applicant.objects.all()
    announcement_list = Announcement.objects.all()
    return render(request, 'fevama/assistance_modify.html', {
        'assistance': assistance,
        'line_list': line_list,
        'act_list': act_list,
        'organism_list': organism_list,
        'situation_list': situation_list,
        'applicant_list': applicant_list,
        'announcement_list': announcement_list
    })

def assistance_modifyItem(request):
    id = request.GET['id']
    line = request.GET['line']
    line = Line.objects.filter(id=line).first()
    act = request.GET['act']
    act = Act.objects.filter(id=act).first()
    organism = request.GET['organism']
    organism = Organism.objects.filter(id=organism).first()
    situation = request.GET['situation']
    situation = Situation.objects.filter(id=situation).first()
    applicant = request.GET['applicant']
    applicant = Applicant.objects.filter(id=applicant).first()
    announcement = request.GET['announcement']
    announcement = Announcement.objects.filter(id=announcement).first()
    management = request.GET['management']
    requested = request.GET['requested']
    applied = request.GET['applied']
    date = request.GET['date']
    payment = request.GET['payment']
    check = Assistance.objects.filter(line=line, act=act, organism=organism, situation=situation, applicant=applicant, management=management, requested=requested, applied=applied, date=date, payment=payment).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    
    check = Assistance.objects.filter(id=id).first()
    if check:
        check.line = line
        check.act = act
        check.organism = organism
        check.situation = situation
        check.applicant = applicant
        check.management = management
        check.requested = requested
        check.applied = applied
        check.date = date
        check.payment = payment
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)
# ----------- END ASSISTANCE ----------------------------- #

# ----------- START LINE ----------------------------- #
def line_index(request):
    object_list = Line.objects.all()
    return render(request, 'fevama/line_list.html', {
        'object_list': object_list
    })

def line_create(request):
    return render(request, 'fevama/line_create.html', {
    })

def line_deleteItem(request):
    id = request.GET['data']
    check = Line.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def line_createItem(request):
    line = request.GET['line']
    check = Line.objects.filter(line=line).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Line.objects.create_line(line)
    
    response = { 'code': 200}
    return JsonResponse(response)

def line_modify(request, id):
    line = Line.objects.filter(id=id).first()
    return render(request, 'fevama/line_modify.html', {
        'line': line
    })

def line_modifyItem(request):
    id = request.GET['id']
    line = request.GET['line']
    lines = Line.objects.all()
    for l in lines:
        if str(l.line) == str(line):
            response = { 'code': 404 }
            return JsonResponse(response)
    
    check = Line.objects.filter(id=id).first()
    if check:
        check.line = line
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)
# ----------- END LINE ----------------------------- #

# ----------- START ACT ----------------------------- #
def act_index(request):
    object_list = Act.objects.all()
    return render(request, 'fevama/act_list.html', {
        'object_list': object_list
    })

def act_deleteItem(request):
    id = request.GET['data']
    check = Act.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def act_create(request):
    return render(request, 'fevama/act_create.html', {
    })

def act_createItem(request):
    act = request.GET['act']
    check = Act.objects.filter(name=act).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Act.objects.create_act(act)
    
    response = { 'code': 200}
    return JsonResponse(response)

def act_modify(request, id):
    act = Act.objects.filter(id=id).first()
    return render(request, 'fevama/act_modify.html', {
        'act': act
    })

def act_modifyItem(request):
    id = request.GET['id']
    act = request.GET['act']
    acts = Act.objects.all()
    for a in acts:
        if str(a.name) == str(act):
            response = { 'code': 404 }
            return JsonResponse(response)
    
    check = Act.objects.filter(id=id).first()
    if check:
        check.name = act
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)
# ----------- END ACT ----------------------------- #

#### RECURSOS HUMANOS ####
def planificacion_index(request):
    return render(request, 'fevama/planificacion_index.html')

# ----------- START APPLICANT ----------------------------- #
def applicant_index(request):
    object_list = Applicant.objects.all()
    return render(request, 'fevama/applicant_list.html', {
        'object_list': object_list
    })

def applicant_create(request):
    return render(request, 'fevama/applicant_create.html', {
    })

def applicant_deleteItem(request):
    id = request.GET['data']
    check = Applicant.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def applicant_createItem(request):
    name = request.GET['data']
    check = Applicant.objects.filter(name=name).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Applicant.objects.create_applicant(name)
    
    response = { 'code': 200}
    return JsonResponse(response)

def applicant_modify(request, id):
    applicant = Applicant.objects.filter(id=id).first()
    return render(request, 'fevama/applicant_modify.html', {
        'applicant': applicant
    })

def applicant_modifyItem(request):
    id = request.GET['id']
    applicant = request.GET['applicant']
    applicants = Applicant.objects.all()
    for a in applicants:
        if applicant.upper() == a.name.upper():
            response = { 'code': 404 }
            return JsonResponse(response)
    
    check = Applicant.objects.filter(id=id).first()
    if check:
        check.name = applicant
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)

# ----------- END APPLICANT ----------------------------- #

# ----------- START ORGANISM ----------------------------- #
def organism_index(request):
    object_list = Organism.objects.all()
    return render(request, 'fevama/organism_list.html', {
        'object_list': object_list
    })

def organism_deleteItem(request):
    id = request.GET['data']
    check = Organism.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def organism_create(request):
    return render(request, 'fevama/organism_create.html', {
    })

def organism_createItem(request):
    name = request.GET['data']
    check = Organism.objects.filter(name=name).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Organism.objects.create_organism(name)
    
    response = { 'code': 200}
    return JsonResponse(response)

def organism_modify(request, id):
    organism = Organism.objects.filter(id=id).first()
    return render(request, 'fevama/organism_modify.html', {
        'organism': organism
    })

def organism_modifyItem(request):
    id = request.GET['id']
    organism = request.GET['organism']
    organisms = Organism.objects.all()
    for o in organisms:
        if organism.upper() == o.name.upper():
            response = { 'code': 404 }
            return JsonResponse(response)
    
    check = Organism.objects.filter(id=id).first()
    if check:
        check.name = organism
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)

# ----------- END ORGANISM ----------------------------- #

# ----------- START SITUATION ----------------------------- #
def situation_index(request):
    object_list = Situation.objects.all()
    return render(request, 'fevama/situation_list.html', {
        'object_list': object_list
    })

def situation_deleteItem(request):
    id = request.GET['data']
    check = Situation.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def situation_create(request):
    return render(request, 'fevama/situation_create.html', {
    })

def situation_createItem(request):
    name = request.GET['data']
    check = Situation.objects.filter(situation=name).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Situation.objects.create_situation(name)
    
    response = { 'code': 200}
    return JsonResponse(response)

def situation_modify(request, id):
    situation = Situation.objects.filter(id=id).first()
    return render(request, 'fevama/situation_modify.html', {
        'situation': situation
    })

def situation_modifyItem(request):
    id = request.GET['id']
    situation = request.GET['situation']
    situations = Situation.objects.all()
    for s in situations:
        if situation.upper() == s.situation.upper():
            response = { 'code': 404 }
            return JsonResponse(response)
    
    check = Situation.objects.filter(id=id).first()
    if check:
        check.situation = situation
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)
# ----------- END SITUATION ----------------------------- #

# ----------- START ANNOUNCEMENT ----------------------------- #
def announcement_index(request):
    object_list = Announcement.objects.all()
    return render(request, 'fevama/announcement_list.html', {
        'object_list': object_list
    })

def announcement_deleteItem(request):
    id = request.GET['data']
    check = Announcement.objects.filter(id=id).first()
    if check:
        check.delete()
    
    response = { 'code': 200}
    return JsonResponse(response)

def announcement_create(request):
    return render(request, 'fevama/announcement_create.html', {
    })

def announcement_createItem(request):
    year = request.GET['data']
    check = Announcement.objects.filter(year=year).first()
    if check:
        response = { 'code': 404 }
        return JsonResponse(response)
    else:
        Announcement.objects.create_announcement(year)
    
    response = { 'code': 200}
    return JsonResponse(response)

def announcement_modify(request, id):
    announcement = Announcement.objects.filter(id=id).first()
    return render(request, 'fevama/announcement_modify.html', {
        'announcement': announcement
    })

def announcement_modifyItem(request):
    id = request.GET['id']
    year = request.GET['year']
    announcements = Announcement.objects.all()
    for a in announcements:
        if int(year) == int(a.year):
            response = { 'code': 404 }
            return JsonResponse(response)
    
    check = Announcement.objects.filter(id=id).first()
    if check:
        check.year = year
        check.save()

    response = { 'code': 200}
    return JsonResponse(response)
# ----------- END ANNOUNCEMENT ----------------------------- #

#### NOTIFICACIONES ####
def notificaciones_index(request):
    return render(request, 'fevama/notificaciones_index.html')

#### BASE DE DATOS ####
def bd_index(request):
    return render(request, 'fevama/bd_index.html')

def BDconfiguration_index(request):
    NextBackupTimePeriod_selected = ConfigParameters.objects.filter(address="NextBackupTimePeriod").first()
    if not NextBackupTimePeriod_selected:
        ConfigParameters.objects.create_configParameter("NextBackupTimePeriod", "12")
        NextBackupTimePeriod_selected = "12"
    NextBackupTimePeriod = ConfigParameters.objects.filter(address="NextBackupTime").first()
    if not NextBackupTimePeriod:
        now = datetime.datetime.now()
        timestamp = int(round(now.timestamp()))
        date = timestamp + 31556926
        ConfigParameters.objects.create_configParameter("NextBackupTime", date)
        date = datetime.datetime.fromtimestamp(int(date))
    else:
        date = datetime.datetime.fromtimestamp(int(NextBackupTimePeriod.value))

    # Backup Files
    files = os.listdir("/home/ubuntu/app/databaseBackups/compressed/")
    list_backup_files = []
    if files != []:
        for file in files:
            list_backup_files.append(file)
    else:
        list_backup_files = ["Esperando primera copia de seguridad..."]

    backup_file = ConfigParameters.objects.filter(address="backupFile").first()
    if backup_file == "None":
        backup_file.value = list_backup_files[0]
        backup_file.save()

    # Contact files
    files = os.listdir("/home/ubuntu/app/csv/Contacts/")
    list_contact_files = []
    if files != []:
        for file in files:
            list_contact_files.append(file)
    else:
        list_contact_files = ["Esperando primera copia de seguridad..."]

    contact_file = ConfigParameters.objects.filter(address="contact_file").first()
    if contact_file == "None":
        contact_file.value = list_contact_files[0]
        contact_file.save()

    # Economic data files
    files = os.listdir("/home/ubuntu/app/csv/EconomicData/")
    list_economic_files = []
    if files != []:
        for file in files:
            list_economic_files.append(file)
    else:
        list_economic_files = ["Esperando primera copia de seguridad..."]

    economic_file = ConfigParameters.objects.filter(address="economic_file").first()
    if economic_file == "None":
        economic_file.value = list_economic_files[0]
        economic_file.save()

    # Selected files
    backup_file = ConfigParameters.objects.filter(address="backupFile").first()
    if backup_file:
        backup_file = backup_file.value
    else:
        ConfigParameters.objects.create_configParameter("backupFile", "none")
        
    economic_file = ConfigParameters.objects.filter(address="economic_file").first()
    if economic_file:
        economic_file = economic_file.value
    else:
        ConfigParameters.objects.create_configParameter("economic_file", "none")

    contact_file = ConfigParameters.objects.filter(address="contact_file").first()
    if contact_file:
        contact_file = contact_file.value
    else:
        ConfigParameters.objects.create_configParameter("contact_file", "none")

    return render(request, 'fevama/BDconfiguration.html', {
        'NextBackupTimePeriod_selected': NextBackupTimePeriod_selected.value,
        'date': date,
        'list_economic_files': list_economic_files,
        'list_contact_files': list_contact_files,
        'list_backup_files': list_backup_files,
        'backup_file': backup_file,
        'economic_file': economic_file,
        'contact_file': contact_file
    })

@csrf_protect
def change_bcfile(request):
    """
    Modify Backup file
    :param request:
    """
    print("CHANGE BC FILE")
    # Contact file
    contact_file = ConfigParameters.objects.filter(address="contact_file").first()
    contact_file.value = request.GET['contactFile']
    contact_file.save()
    # Economic file
    economic_file = ConfigParameters.objects.filter(address="economic_file").first()
    economic_file.value = request.GET['economicFile']
    economic_file.save()
    # Backup file
    backup_file = ConfigParameters.objects.filter(address="backupFile").first()
    backup_file.value = request.GET['backupFile']
    backup_file.save()

    return redirect('/fevama/BDconfiguration_index')

def last_backup(request):
    """
    Download data from the last automatic backup
    :param request:
    """

    file = ConfigParameters.objects.filter(address="backupFile").first()
    filename = file.value
    filepath = '/home/ubuntu/app/databaseBackups/compressed/' + filename
    if (os.path.isfile(filepath)):
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

    return redirect('/fevama/BDconfiguration_index')

def last_economicData(request):
    """
    Download data from the last automatic economic data
    :param request:
    """

    file = ConfigParameters.objects.filter(address="economic_file").first()
    filename = file.value
    filepath = '/home/ubuntu/app/csv/EconomicData/' + filename
    if (os.path.isfile(filepath)):
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

    return redirect('/fevama/BDconfiguration_index')

def last_contacts(request):
    """
    Download data from the last automatic contact data
    :param request:
    """

    file = ConfigParameters.objects.filter(address="contact_file").first()
    filename = file.value
    filepath = '/home/ubuntu/app/csv/Contacts/' + filename
    if (os.path.isfile(filepath)):
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

    return redirect('/fevama/BDconfiguration_index')
    

def execute_backup(request):
    os.system('./backupDatabase.sh')
    filename = 'backup.gz'
    filepath = '/home/ubuntu/app/media/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename

    return response

def backup_upload(request):
    if request.method == 'POST' and 'backupFile' in  request.FILES and request.FILES['backupFile']:
        myFile = request.FILES['backupFile']
        fs = FileSystemStorage()
        if fs.exists("backup.gz"):
            fs.delete("backup.gz")
        fs.save("backup.gz", myFile)
        return redirect('/fevama/BDconfiguration_index')
    return redirect('/fevama/BDconfiguration_index')

def restore_database(request):
    response = {'code': 404}
    if (os.path.isfile("/home/ubuntu/app/media/backup.gz")):

        # Ejecutamos la restauración
        os.system('./restoreDatabase.sh')
        response = {'code': 200}

    return JsonResponse(response)

def modify_bdconfig(request):
    """
    Modify BDD
    :param request:
    """

    postContent = request.GET
    aux = postContent['NextBackupTimePeriod']
    now = datetime.datetime.now()
    timestamp = int(round(now.timestamp()))

    if (aux == "12"):
        timestamp = timestamp + 31556926
    elif (aux == "6"):
        timestamp = timestamp + 6*2629743
    elif (aux == "3"):
        timestamp = timestamp + 3*2629743
    elif (aux == "1"):
        timestamp = timestamp + 2629743

    ConfigParameters.objects.update_config_parameter('NextBackupTimePeriod', postContent['NextBackupTimePeriod'])
    ConfigParameters.objects.update_config_parameter('NextBackupTime', timestamp)

    response = {'code': 200}
    return JsonResponse(response)

#### PARAMETROS ####
def parametros_index(request):
    return render(request, 'fevama/parametros_index.html')
 