from django.urls import path
from rest_framework.authtoken import views as authviews
from api import views

app_name = 'api'
urlpatterns = [

    # ------------------ AUTH --------------------------- #
    path('api-token-auth/', authviews.obtain_auth_token),

]