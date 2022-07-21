from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
import mysql.connector as sql
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
 

em=''
pwd=''


# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'App_auth/home.html')




@csrf_exempt
def welcome(request):
    return render(request, 'App_auth/welcome.html')

@csrf_exempt
def login_or_signup(request):
    return render(request, 'App_auth/login_or_signup.html')





@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_auth:login-or-signup'))

