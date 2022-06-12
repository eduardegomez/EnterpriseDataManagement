#scripts/backupDatabase.py

from email import header
from http.client import OK
from fevama.views import *
from django.db.models import Q
import os
from datetime import datetime
import csv

def run():

    NextBackupTimePeriod_selected = ConfigParameters.objects.filter(address="NextBackupTimePeriod").first()
    NextBackupTimePeriod_selected = NextBackupTimePeriod_selected.value
    NextBackupTimePeriod = ConfigParameters.objects.filter(address="NextBackupTime").first()
    timestamp =  NextBackupTimePeriod.value

    current = datetime.now().timestamp()
    date = datetime.now().strftime("%Y%m%dT%H")
    nameEconomicData = date + ".csv"
    nameContacts =  date + ".csv"

    path1 = "/home/ubuntu/app/csv/EconomicData/"
    path2 = "/home/ubuntu/app/csv/Contacts/"
    pathBck = "/home/ubuntu/app/databaseBackups/compressed/"

    if int(timestamp) <= current:

        # Comprobar si existen los directorios, sino los creamos
        if os.path.exists(path1) == False:
            os.mkdir(path1)
        if os.path.exists(path2) == False:
            os.mkdir(path2)
        if os.path.exists(pathBck) == False:
            os.mkdir(pathBck)

        # Comprobar que sólo estemos guardando los 5 últimos archivos
        checkLast5(path1, date, ".csv")
        checkLast5(path2, date, ".csv")
        checkLast5(pathBck, date, ".gz")

        # Generar CSV Economic Data
        objects = EconomicData.objects.all()
        create_csv(objects, "economicData", path1, nameEconomicData)

        # Generar CSV Contacts
        objects = Contact.objects.all()
        create_csv(objects, "contact", path2, nameContacts)

        # Ejecutar backup y actualizar campos para el siguiente programado
        os.system('sudo ./backupDatabaseCompressed.sh')
        print("Backup done")

        timestamp = int(datetime.now().timestamp())

        if (NextBackupTimePeriod_selected == "12"):
            timestamp = timestamp + 31556926
        elif (NextBackupTimePeriod_selected == "6"):
            timestamp = timestamp + 6*2629743
        elif (NextBackupTimePeriod_selected == "3"):
            timestamp = timestamp + 3*2629743
        elif (NextBackupTimePeriod_selected == "1"):
            timestamp = timestamp + 2629743
        
        ConfigParameters.objects.update_config_parameter('NextBackupTime', timestamp)

    else:
        print("Not ready")

def checkLast5(path, date, type):
    """
    Comprobar si existen más de 4 archivos en el directorio
    Para nunca tener almacenados más de 5 archivos
    """

    files_node = os.listdir(path)
    list_files_node = []
    old_file = date + type
    if files_node != []:
        for file in files_node:
            list_files_node.append(file)
            if file < old_file:
                old_file = file

    if len(list_files_node) >= 5:
        old_file = path + old_file
        os.remove(old_file)

    response = {'code': 200}
    return JsonResponse(response)

def create_csv(objects, type, path, name):

    if (type == "economicData"):
        if objects:
            new_report = open(path+name,"w")
            header = "Año"+";"+"Trabajadores"+";"+"Valor facturación"+";"+"Empresa"+"\n"
            new_report.write(header)

            for d in objects:
                meterD = str(d.year)
                meterD += ';' + str(d.workers)
                meterD += ';' + str(d.data)
                meterD += ';' + str(d.empresa.name)
                meterD += '\n'

                new_report.write(meterD)

        else:
            print("No economic data")

    elif (type == "contact"):
        if objects:
            new_report = open(path+name,"w")
            header = "Nombre"+";"+"Email"+";"+"Empresa"+";"+"Tipo"+"\n"
            new_report.write(header)
            for d in objects:
                meterD = str(d.name)
                meterD += ';' + str(d.email)
                meterD += ';' + str(d.empresa.name)
                meterD += ';' + str(d.type.name)
                meterD += '\n'
                new_report.write(meterD)
        else:
            print("No contact data")

    response = {'code': 200}
    return JsonResponse(response)