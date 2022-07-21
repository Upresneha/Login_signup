import email
from django import conf
from django.shortcuts import render
import mysql.connector as sql
from django.core.mail import send_mail
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.views.decorators.csrf import csrf_exempt

from verify_email.email_handler import send_verification_email
from django.contrib.auth import get_user_model
from django_email_verification import confirm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

fn=''
ln=''
s=''
em=''
pwd=''


@csrf_exempt
def reset(request):
    return render(request, 'App_auth/forgot.html')

def signupaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password='Sneha@123',db="website")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
          
        c="INSERT INTO users VALUES('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        send_mail(
            'Camel party',
            'you are succesfully Registered... please click on link to login http://127.0.0.1:8000/accounts/login-or-signup/',
            'upresneha123@gmail.come',
            [em],
            fail_silently=False,
        )

        cursor.execute(c)
        m.commit()  
        return render(request,'./App_auth/mail_body.html')
        # return render(request,'./App_auth/mail_body.html')      
    return render(request,'./App_auth/signup.html')
def loginaction(request):

    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password='Sneha@123',db="website")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            
        c="SELECT * FROM  users WHERE email='{}' AND password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'./App_auth/error.html')
        else:
            return render(request,'./App_auth/welcome.html')
    return render(request,'./App_auth/signup.html')

# @csrf_exempt
# def sendEmail(request):
#     password=request.POST.get('password')
#     # username=request.POST.get('username')
#     email=request.POST.get('email')
#     user=get_user_model().objects.create(password=password,email=email)
#     confirm(user)
#     return render(request,'App_auth/welcome.html')



 


