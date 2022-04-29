from django.urls import path
from .views import PasswordsChangeView
from . import views

from fevama import views

app_name = 'fevama'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('password/', PasswordsChangeView.as_view(template_name="fevama/change-password.html"), name="password"),
    path('password_success/', views.password_success, name="password_success"),

    # -------- EMPRESAS -------- #
    path('projects_index/', views.projects_index, name="projects_index"),

    # EMPRESA
    path('empresas_index/', views.empresas_index, name="empresas_index"),

    # CONTACT
    path('contact/', views.contact_index, name="contact_index"),

    # TYPE OF CONTACT
    path('typeofcontact_index/', views.typeofcontact_index, name="typeofcontact_index"),
    path('typeofcontact_create/', views.typeofcontact_create, name="typeofcontact_create"),
    path('typeofcontact_createItem/', views.typeofcontact_createItem, name="typeofcontact_createItem"),
    path('typeofcontact_deleteItem/', views.typeofcontact_deleteItem, name="typeofcontact_deleteItem"),
    path('typeofcontact_modify/<id>', views.typeofcontact_modify, name="typeofcontact_modify"),
    path('typeofcontact_modifyItem/', views.typeofcontact_modifyItem, name="typeofcontact_modifyItem"),
    
    # ECONOMIC DATA
    path('economicdata_index/', views.economicdata_index, name="economicdata_index"),
    

    # -------- AYUDAS -------- #
    path('ayudas_index/', views.ayudas_index, name="ayudas_index"),

    # -------- PLANIFICACIÓN -------- #
    path('planificacion_index/', views.planificacion_index, name="planificacion_index"),

    # -------- NOTIFICACIONES -------- #
    path('notificaciones_index/', views.notificaciones_index, name="notificaciones_index"),

    # -------- BASE DE DATOS -------- #
    path('bd_index/', views.bd_index, name="bd_index"),

    # -------- PARAMETROS -------- #
    path('parametros_index/', views.parametros_index, name="parametros_index"),
]

