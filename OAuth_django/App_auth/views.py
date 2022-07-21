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


# @csrf_exempt
# def login_signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(username=email, password=password)
#         if user:
#             login(request, user)
#             return HttpResponseRedirect(reverse('App_auth:home'))
#         else:
#             createUser = User(username=email)
#             createUser.set_password(password)
#             createUser.save()
#             user = authenticate(username=email, password=password)
#             login(request, user)
#             return HttpResponseRedirect(reverse('App_auth:home'))

#     return HttpResponseRedirect(reverse('App_auth:login-signup'))



# Create your views here.


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_auth:login-or-signup'))

