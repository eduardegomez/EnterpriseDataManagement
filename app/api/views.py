from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from fevama.views import *

# Visalizar, modificar y borrar empresas
@api_view(['GET','PUT','DELETE'])
def empresas(request):
    if request.method == 'GET':
        empresas_response = []
        empresas = Empresa.objects.all()
        if empresas:
            for e in empresas:
                empresa_list = dict()
                empresa_list["ID"] = e.id
                empresa_list["Nombre"] = e.name
                empresa_list["CIF"] = e.cif
                empresa_list["CNAE"] = e.cnae
                empresa_list["Teléfono"] = e.phone
                empresa_list["Observaciones"] = e.aux
                empresas_response.append(empresa_list)

            return JsonResponse(empresas_response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay empresas registradas en el sistema", status=404, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado la empresa", status=404, safe=False)

        empresa = Empresa.objects.filter(id=id).first()
        if empresa:
            if "Nombre" in data:
                empresa.name = data["Nombre"]
            if "CIF" in data:
                empresa.cif = data["CIF"]
            if "CNAE" in data:
                empresa.cnae = data["CNAE"]
            if "Teléfono" in data:
                empresa.phone = data["Teléfono"]
            if "Observaciones" in data:
                empresa.aux = data["Observaciones"]

            empresa.save()
            empresa_list = dict()
            empresa_list["ID"] = empresa.id
            empresa_list["Nombre"] = empresa.name
            empresa_list["CIF"] = empresa.cif
            empresa_list["CNAE"] = empresa.cnae
            empresa_list["Teléfono"] = empresa.phone
            empresa_list["Observaciones"] = empresa.aux

            return JsonResponse(empresa_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado la empresa", status=404, safe=False)


    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado la empresa", status=404, safe=False)

        empresa = Empresa.objects.filter(id=id).first()
        if empresa:
            empresa_list = dict()
            empresa_list["ID"] = empresa.id
            empresa_list["Nombre"] = empresa.name
            empresa_list["CIF"] = empresa.cif
            empresa_list["CNAE"] = empresa.cnae
            empresa_list["Teléfono"] = empresa.phone
            empresa_list["Observaciones"] = empresa.aux
            empresa.delete()

            return JsonResponse(empresa_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado la empresa", status=404, safe=False)

# Visalizar, modificar y borrar contactos
@api_view(['GET','DELETE'])
def contacts(request):
    if request.method == 'GET':
        contacts_response = []
        contacts = Contact.objects.all()
        if contacts:
            for c in contacts:
                contact_list = dict()
                contact_list["ID"] = c.id
                contact_list["Nombre"] = c.name
                contact_list["Email"] = c.email
                empresa = Empresa.objects.filter(id=c.empresa_id).first()
                contact_list["Empresa"] = empresa.name
                type = TypeOfContact.objects.filter(id=c.type_id).first()
                contact_list["Tipo"] = type.name
                contacts_response.append(contact_list)

            return JsonResponse(contacts_response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay contactos registrados en el sistema", status=404, safe=False)

    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado el contacto", status=404, safe=False)

        c = Contact.objects.filter(id=id).first()
        if c:
            contact_list = dict()
            contact_list["ID"] = c.id
            contact_list["Nombre"] = c.name
            contact_list["Email"] = c.email
            empresa = Empresa.objects.filter(id=c.empresa_id).first()
            contact_list["Empresa"] = empresa.name
            type = TypeOfContact.objects.filter(id=c.type_id).first()
            contact_list["Tipo"] = type.name
            c.delete()

            return JsonResponse(contact_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado el contacto", status=404, safe=False)

# Visalizar y borrar tipos contactos
@api_view(['GET','DELETE'])
def typeofcontacts(request):
    if request.method == 'GET':
        typeofcontacts_response = []
        tipes = TypeOfContact.objects.all()
        if tipes:
            for t in tipes:
                typecontact_list = dict()
                typecontact_list["ID"] = t.id
                typecontact_list["Nombre"] = t.name
                typeofcontacts_response.append(typecontact_list)

            return JsonResponse(typeofcontacts_response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay tipos de contactos registrados en el sistema", status=404, safe=False)

    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado el tipo de contacto", status=404, safe=False)

        t = TypeOfContact.objects.filter(id=id).first()
        if t:
            typecontact_list = dict()
            typecontact_list["ID"] = t.id
            typecontact_list["Nombre"] = t.name
            t.delete()

            return JsonResponse(typecontact_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado el tipo de contacto", status=404, safe=False)

# Visalizar, modificar y borrar datos económicos
@api_view(['GET','PUT','DELETE'])
def economicdata(request):
    if request.method == 'GET':
        response = []
        economic = EconomicData.objects.all()
        if economic:
            for e in economic:
                data_list = dict()
                data_list["ID"] = e.id
                empresa = Empresa.objects.filter(id=e.empresa_id).first()
                data_list["Empresa"] = empresa.name
                data_list["Convocatoria"] = e.year
                data_list["Trabajadores"] = e.workers
                data_list["Valor anual"] = e.data
                response.append(data_list)

            return JsonResponse(response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay datos económicos registrados en el sistema", status=404, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha los datos económicos", status=404, safe=False)

        e = EconomicData.objects.filter(id=id).first()
        if e:
            if "Trabajadores" in data:
                e.workers = data["Trabajadores"]
            if "Valor anual" in data:
                e.data = data["Valor anual"]

            data_list = dict()
            data_list["ID"] = e.id
            empresa = Empresa.objects.filter(id=e.empresa_id).first()
            data_list["Empresa"] = empresa.name
            data_list["Convocatoria"] = e.year
            data_list["Trabajadores"] = e.workers
            data_list["Valor anual"] = e.data
            e.save()

            return JsonResponse(data_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha los datos económicos", status=404, safe=False)

    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha los datos económicos", status=404, safe=False)

        e = EconomicData.objects.filter(id=id).first()
        if e:
            data_list = dict()
            data_list["ID"] = e.id
            empresa = Empresa.objects.filter(id=e.empresa_id).first()
            data_list["Empresa"] = empresa.name
            data_list["Convocatoria"] = e.year
            data_list["Trabajadores"] = e.workers
            data_list["Valor anual"] = e.data
            e.delete()

            return JsonResponse(data_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha los datos económicos", status=404, safe=False)

# Visalizar y borrar proyectos
@api_view(['GET','DELETE'])
def projects(request):
    if request.method == 'GET':
        response = []
        projects = Project.objects.all()
        if projects:
            for p in projects:
                data_list = dict()
                data_list["ID"] = p.id
                empresa = Empresa.objects.filter(id=p.empresa_id).first()
                data_list["Empresa"] = empresa.name
                data_list["Nombre proyecto"] = p.project_name
                announcement = Announcement.objects.filter(id=p.announcement_id).first()
                data_list["Convocatoria"] = announcement.year
                response.append(data_list)

            return JsonResponse(response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay proyectos registrados en el sistema", status=404, safe=False)


    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado el proyecto", status=404, safe=False)

        p = Project.objects.filter(id=id).first()
        if p:
            data_list = dict()
            data_list["ID"] = p.id
            empresa = Empresa.objects.filter(id=p.empresa_id).first()
            data_list["Empresa"] = empresa.name
            data_list["Nombre proyecto"] = p.project_name
            announcement = Announcement.objects.filter(id=p.announcement_id).first()
            data_list["Convocatoria"] = announcement.year
            p.delete()

            return JsonResponse(data_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado el proyecto", status=404, safe=False)

# Visalizar y borrar facturas
@api_view(['GET','DELETE'])
def invoices(request):
    if request.method == 'GET':
        response = []
        invoices = Invoice.objects.all()
        if invoices:
            for p in invoices:
                data_list = dict()
                data_list["ID"] = p.id
                data_list["Numero"] = p.number
                data_list["Factura"] = p.invoice
                data_list["Convocatoria"] = p.year
                data_list["Cantidad"] = p.amount
                project = Project.objects.filter(id=p.project_id).first()
                data_list["Proyecto"] = project.project_name
                response.append(data_list)

            return JsonResponse(response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay facturas registradas en el sistema", status=404, safe=False)

    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado la factura", status=404, safe=False)

        p = Invoice.objects.filter(id=id).first()
        if p:
            data_list = dict()
            data_list["ID"] = p.id
            data_list["Numero"] = p.number
            data_list["Factura"] = p.invoice
            data_list["Convocatoria"] = p.year
            data_list["Cantidad"] = p.amount
            project = Project.objects.filter(id=p.project_id).first()
            data_list["Proyecto"] = project.project_name
            p.delete()

            return JsonResponse(data_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado la factura", status=404, safe=False)

# Visalizar y borrar ayudas
@api_view(['GET','DELETE'])
def assistances(request):
    if request.method == 'GET':
        response = []
        assistances = Assistance.objects.all()
        if assistances:
            for p in assistances:
                data_list = dict()
                data_list["ID"] = p.id
                data_list["Gestionado"] = p.management
                data_list["Solicitado"] = p.requested
                data_list["Aplicado"] = p.applied
                data_list["Fecha de resolución"] = p.date
                data_list["Fecha de cobro"] = p.payment
                act = Act.objects.filter(id=p.act_id).first()
                data_list["Fecha de cobro"] = act.name
                announcement = Announcement.objects.filter(id=p.announcement_id).first()
                data_list["Convocatoria"] = announcement.year
                project = Project.objects.filter(id=p.project_id).first()
                data_list["Proyecto"] = project.project_name
                applicant = Applicant.objects.filter(id=p.applicant_id).first()
                data_list["Solicitante"] = applicant.name
                line = Line.objects.filter(id=p.line_id).first()
                data_list["Linea de ayuda"] = line.line
                organism = Organism.objects.filter(id=p.organism_id).first()
                data_list["Organismo"] = organism.name
                situation = Situation.objects.filter(id=p.organism_id).first()
                data_list["Situación"] = situation.situation

                response.append(data_list)

            return JsonResponse(response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay ayudas registradas en el sistema", status=404, safe=False)

    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado la ayuda", status=404, safe=False)

        p = Assistance.objects.filter(id=id).first()
        if p:
            data_list = dict()
            data_list["ID"] = p.id
            data_list["Gestionado"] = p.management
            data_list["Solicitado"] = p.requested
            data_list["Aplicado"] = p.applied
            data_list["Fecha de resolución"] = p.date
            data_list["Fecha de cobro"] = p.payment
            act = Act.objects.filter(id=p.act_id).first()
            data_list["Fecha de cobro"] = act.name
            announcement = Announcement.objects.filter(id=p.announcement_id).first()
            data_list["Convocatoria"] = announcement.year
            project = Project.objects.filter(id=p.project_id).first()
            data_list["Proyecto"] = project.project_name
            applicant = Applicant.objects.filter(id=p.applicant_id).first()
            data_list["Solicitante"] = applicant.name
            line = Line.objects.filter(id=p.line_id).first()
            data_list["Linea de ayuda"] = line.line
            organism = Organism.objects.filter(id=p.organism_id).first()
            data_list["Organismo"] = organism.name
            situation = Situation.objects.filter(id=p.organism_id).first()
            data_list["Situación"] = situation.situation
            p.delete()

            return JsonResponse(data_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado la ayuda", status=404, safe=False)

# Visalizar y borrar linea de ayuda
@api_view(['GET','DELETE'])
def line(request):
    if request.method == 'GET':
        response = []
        lines = Line.objects.all()
        if lines:
            for p in lines:
                data_list = dict()
                data_list["ID"] = p.id
                data_list["Linea de ayuda"] = p.line

                response.append(data_list)

            return JsonResponse(response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay lineas de ayuda registradas en el sistema", status=404, safe=False)

    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        if "ID" in data:
            id = data["ID"]
        else:
            return JsonResponse("No se ha encontrado la linea de ayuda", status=404, safe=False)

        p = Line.objects.filter(id=id).first()
        if p:
            data_list = dict()
            data_list["ID"] = p.id
            data_list["Linea de ayuda"] = p.line
            p.delete()

            return JsonResponse(data_list, status=200, safe=False)
        
        else:
            return JsonResponse("No se ha encontrado la linea de ayuda", status=404, safe=False)