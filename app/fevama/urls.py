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

    # -------- CUADROS DE MANDO -------- #
    path('management_index/', views.management_index, name="management_index"),

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

    path('anualdata_graphs/', views.anualdata_graphs, name="anualdata_graphs"),
    path('anualdata_getdatagraph/', views.anualdata_getdatagraph, name="anualdata_getdatagraph"),

    path('line_graphs/', views.line_graphs, name="line_graphs"),
    path('line_getdatagraph/', views.line_getdatagraph, name="line_getdatagraph"), 

    # -------- SUBVENCIONES -------- #
    path('ayudas_index/', views.ayudas_index, name="ayudas_index"),

    # PROYECTOS
    path('project_index/', views.project_index, name="project_index"),
    path('project_deleteItem/', views.project_deleteItem, name="project_deleteItem"),
    path('project_create/', views.project_create, name="project_create"),
    path('project_createItem/', views.project_createItem, name="project_createItem"),
    path('project_modify/<id>', views.project_modify, name="project_modify"),
    path('project_modifyItem/', views.project_modifyItem, name="project_modifyItem"),

    # FACTURAS
    path('invoice_index/', views.invoice_index, name="invoice_index"),
    path('invoice_deleteItem/', views.invoice_deleteItem, name="invoice_deleteItem"),
    path('invoice_create/', views.invoice_create, name="invoice_create"),
    path('invoice_createItem/', views.invoice_createItem, name="invoice_createItem"),
    path('invoice_modify/<id>', views.invoice_modify, name="invoice_modify"),
    path('invoice_modifyItem/', views.invoice_modifyItem, name="invoice_modifyItem"),

    # AYUDAS
    path('assistance_index/', views.assistance_index, name="assistance_index"),
    path('assistance_deleteItem/', views.assistance_deleteItem, name="assistance_deleteItem"),
    path('assistance_create/', views.assistance_create, name="assistance_create"),
    path('assistance_createItem/', views.assistance_createItem, name="assistance_createItem"),
    path('assistance_modify/<id>', views.assistance_modify, name="assistance_modify"),
    path('assistance_modifyItem/', views.assistance_modifyItem, name="assistance_modifyItem"),
    path('assistance_details/<id>', views.assistance_details, name="assistance_details"),
    

    # LINEA DE AYUDAS
    path('line_index/', views.line_index, name="line_index"),
    path('line_deleteItem/', views.line_deleteItem, name="line_deleteItem"),
    path('line_create/', views.line_create, name="line_create"),
    path('line_createItem/', views.line_createItem, name="line_createItem"),
    path('line_modify/<id>', views.line_modify, name="line_modify"),
    path('line_modifyItem/', views.line_modifyItem, name="line_modifyItem"),
    
    # ACTUACIÓN
    path('act_index/', views.act_index, name="act_index"),
    path('act_deleteItem/', views.act_deleteItem, name="act_deleteItem"),
    path('act_create/', views.act_create, name="act_create"),
    path('act_createItem/', views.act_createItem, name="act_createItem"),
    path('act_modify/<id>', views.act_modify, name="act_modify"),
    path('act_modifyItem/', views.act_modifyItem, name="act_modifyItem"),

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

    path('alerts_index/', views.alerts_index, name="alerts_index"),
    path('alert_deleteItem/', views.alert_deleteItem, name="alert_deleteItem"),

    path('notifications_index/', views.notifications_index, name="notifications_index"),
    path('notification_create/', views.notification_create, name="notification_create"),
    path('notification_deleteItem/', views.notification_deleteItem, name="notification_deleteItem"),
    
    

    # -------- BASE DE DATOS -------- #
    path('bd_index/', views.bd_index, name="bd_index"),
    path('BDconfiguration_index/', views.BDconfiguration_index, name="BDconfiguration_index"),
    path('execute_backup/', views.execute_backup, name="execute_backup"),
    path('backup_upload/', views.backup_upload, name="backup_upload"),
    path('restore_database/', views.restore_database, name="restore_database"),
    path('modify_bdconfig/', views.modify_bdconfig, name="modify_bdconfig"),
    path('change_bcfile/', views.change_bcfile, name="change_bcfile"),
    path('last_backup/', views.last_backup, name="last_backup"),
    path('last_economicData/', views.last_economicData, name="last_economicData"),
    path('last_contacts/', views.last_contacts, name="last_contacts"),
    
    path('cleanBD_index/', views.cleanBD_index, name="cleanBD_index"),
    path('cleanData/', views.cleanData, name="cleanData"),

    # -------- PARAMETROS -------- #
    path('parametros_index/', views.parametros_index, name="parametros_index"),
    path('users_index/', views.users_index, name="users_index"),
    path('user_deleteItem/', views.user_deleteItem, name="user_deleteItem"),
    path('user_create/', views.user_create, name="user_create"),
    path('user_createItem/', views.user_createItem, name="user_createItem"),   
]

