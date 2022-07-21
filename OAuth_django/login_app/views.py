from django.shortcuts import render
import mysql.connector as sql

em = ''
pwd = ''


# Create your views here.
def loginaction(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password='Niraj@2396', db="website")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "psw":
                pwd = value

        c = "SELECT * FROM  users WHERE email='{}' AND password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, './App_auth/error.html')
        else:
            return render(request, './App_auth/welcome.html')
    return render(request, './App_auth/signup.html')
