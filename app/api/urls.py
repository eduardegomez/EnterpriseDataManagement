from django.urls import path
from rest_framework.authtoken import views as authviews
from api import views

app_name = 'api'
urlpatterns = [

    # ------------------ AUTH --------------------------- #
    path('api-token-auth/', authviews.obtain_auth_token),

    # ------------------ METHODS --------------------------- #
    path('empresas/', views.empresas),
    path('contacts/', views.contacts),
    path('typeofcontacts/', views.typeofcontacts),
    path('economicdata/', views.economicdata),
    path('projects/', views.projects),
    path('invoices/', views.invoices),
    path('assistances/', views.assistances),
    path('line/', views.line),

]