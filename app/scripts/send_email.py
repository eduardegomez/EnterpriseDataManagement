from django.core.mail import send_mail

from fevama.views import *
from datetime import datetime

def send_email_to(email, type, project_name):

    date = datetime.today().strftime('%Y-%m-%d')
    send_mail(
        'ALERTA FEVAMA',
        str(type) + " PARA EL PROYECTO: " + project_name + " CON FECHA: " + date,
        'notificaciones_fevama@outlook.es',
        [email],
        fail_silently=False
    )

def run():

    alert_list = Alert.objects.filter(notify="0").all()
    for a in alert_list:
        notification_list = Notification.objects.all()
        for n in notification_list:
            if n.type == "ALL":
                send_email_to(n.email,a.type,a.project.project_name)
            elif str(n.type) == str(a.type):
                send_email_to(n.email,a.type,a.project.project_name)
        a.notify = "1"
        a.save()


