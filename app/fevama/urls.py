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
    path('empresa_create/', views.empresa_create, name="empresa_create"),
    path('empresa_createItem/', views.empresa_createItem, name="empresa_createItem"),
    path('empresa_deleteItem/', views.empresa_deleteItem, name="empresa_deleteItem"),
    path('empresa_modify/<id>', views.empresa_modify, name="empresa_modify"),
    path('empresa_modifyItem/', views.empresa_modifyItem, name="empresa_modifyItem"),
    
    # CONTACT
    path('contact/', views.contact_index, name="contact_index"),
    path('contact_create/', views.contact_create, name="contact_create"),
    path('contact_createItem/', views.contact_createItem, name="contact_createItem"),
    path('contact_deleteItem/', views.contact_deleteItem, name="contact_deleteItem"),
    path('contact_modify/<id>', views.contact_modify, name="contact_modify"),
    path('contact_modifyItem/', views.contact_modifyItem, name="contact_modifyItem"),

    # TYPE OF CONTACT
    path('typeofcontact_index/', views.typeofcontact_index, name="typeofcontact_index"),
    path('typeofcontact_showAll/', views.typeofcontact_showAll, name="typeofcontact_showAll"),
    path('typeofcontact_create/', views.typeofcontact_create, name="typeofcontact_create"),
    path('typeofcontact_createItem/', views.typeofcontact_createItem, name="typeofcontact_createItem"),
    path('typeofcontact_deleteItem/', views.typeofcontact_deleteItem, name="typeofcontact_deleteItem"),
    path('typeofcontact_modify/<id>', views.typeofcontact_modify, name="typeofcontact_modify"),
    path('typeofcontact_modifyItem/', views.typeofcontact_modifyItem, name="typeofcontact_modifyItem"),
    
    # ECONOMIC DATA
    path('economicdata_index/', views.economicdata_index, name="economicdata_index"),
    path('economicdata_create/', views.economicdata_create, name="economicdata_create"),
    path('economicdata_createItem/', views.economicdata_createItem, name="economicdata_createItem"),
    path('economicdata_modify/<id>', views.economicdata_modify, name="economicdata_modify"),
    path('economicdata_modifyItem/', views.economicdata_modifyItem, name="economicdata_modifyItem"),
    path('economicdata_deleteItem/', views.economicdata_deleteItem, name="economicdata_deleteItem"),


    # GRAPHS
    path('graphs_index/', views.graphs_index, name="graphs_index"),
    path('empresa_getdatagraph/', views.empresa_getdatagraph, name="empresa_getdatagraph"),
    path('empresa_compare/', views.empresa_compare, name="empresa_compare"),


    # -------- SUBVENCIONES -------- #
    path('ayudas_index/', views.ayudas_index, name="ayudas_index"),

    # PROYECTOS
    path('project_index/', views.project_index, name="project_index"),

    # FACTURAS
    path('invoice_index/', views.invoice_index, name="invoice_index"),

    # AYUDAS
    path('assistance_index/', views.assistance_index, name="assistance_index"),

    # LINEA DE AYUDAS
    path('line_index/', views.line_index, name="line_index"),
    
    # ACTUACIÓN
    path('act_index/', views.act_index, name="act_index"),

    # -------- RECURSOS HUMANOS -------- #
    path('planificacion_index/', views.planificacion_index, name="planificacion_index"),

    # SOLICITANTES
    path('applicant_index/', views.applicant_index, name="applicant_index"),
    path('applicant_deleteItem/', views.applicant_deleteItem, name="applicant_deleteItem"),
    path('applicant_create/', views.applicant_create, name="applicant_create"),
    path('applicant_createItem/', views.applicant_createItem, name="applicant_createItem"),
    path('applicant_modify/<id>', views.applicant_modify, name="applicant_modify"),
    path('applicant_modifyItem/', views.applicant_modifyItem, name="applicant_modifyItem"),

    # ORGANISMO
    path('organism_index/', views.organism_index, name="organism_index"),
    path('organism_deleteItem/', views.organism_deleteItem, name="organism_deleteItem"),
    path('organism_create/', views.organism_create, name="organism_create"), 
    path('organism_createItem/', views.organism_createItem, name="organism_createItem"),
    path('organism_modify/<id>', views.organism_modify, name="organism_modify"),
    path('organism_modifyItem/', views.organism_modifyItem, name="organism_modifyItem"),

    # SITUACIÓN
    path('situation_index/', views.situation_index, name="situation_index"),
    path('situation_deleteItem/', views.situation_deleteItem, name="situation_deleteItem"),
    path('situation_create/', views.situation_create, name="situation_create"), 
    path('situation_createItem/', views.situation_createItem, name="situation_createItem"),
    path('situation_modify/<id>', views.situation_modify, name="situation_modify"),
    path('situation_modifyItem/', views.situation_modifyItem, name="situation_modifyItem"),

    # CONVOCATORIA
    path('announcement_index/', views.announcement_index, name="announcement_index"),
    path('announcement_deleteItem/', views.announcement_deleteItem, name="announcement_deleteItem"),
    path('announcement_create/', views.announcement_create, name="announcement_create"),
    path('announcement_createItem/', views.announcement_createItem, name="announcement_createItem"),
    path('announcement_modify/<id>', views.announcement_modify, name="announcement_modify"),
    path('announcement_modifyItem/', views.announcement_modifyItem, name="announcement_modifyItem"),


    # -------- NOTIFICACIONES -------- #
    path('notificaciones_index/', views.notificaciones_index, name="notificaciones_index"),

    # -------- BASE DE DATOS -------- #
    path('bd_index/', views.bd_index, name="bd_index"),

    # -------- PARAMETROS -------- #
    path('parametros_index/', views.parametros_index, name="parametros_index"),
]

