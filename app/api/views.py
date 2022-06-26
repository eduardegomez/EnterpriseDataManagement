from django.shortcuts import render
from rest_framework.decorators import api_view
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
                empresa_list["Nombre"] = e.name
                empresa_list["CIF"] = e.cif
                empresa_list["CNAE"] = e.cnae
                empresa_list["Teléfono"] = e.phone
                empresa_list["Observaciones"] = e.aux
                empresas_response.append(empresa_list)

            return JsonResponse(empresas_response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay empresas registradas en el sistema", status=404, safe=False)

# Visalizar, modificar y borrar contactos
@api_view(['GET','PUT','DELETE'])
def contacts(request):
    if request.method == 'GET':
        contacts_response = []
        contacts = Contact.objects.all()
        if contacts:
            for c in contacts:
                contact_list = dict()
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

# Visalizar, modificar y borrar tipos contactos
@api_view(['GET','PUT','DELETE'])
def typeofcontacts(request):
    if request.method == 'GET':
        typeofcontacts_response = []
        tipes = Contact.objects.all()
        if tipes:
            for t in tipes:
                typecontact_list = dict()
                typecontact_list["ID"] = t.id
                typecontact_list["Nombre"] = t.name
                typeofcontacts_response.append(typecontact_list)

            return JsonResponse(typeofcontacts_response, status=200, safe=False)
        
        else:
            return JsonResponse("No hay tipos de contactos registrados en el sistema", status=404, safe=False)

