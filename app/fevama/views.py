from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
        pass

# LOGOUT
def logout_view(request):

    logout(request)
    return redirect('/admin/app/login/')

# HOME  
def home(request):

    return render(request, 'fevama/index.html', {})