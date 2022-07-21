from xml.etree.ElementInclude import include
from django.urls import path,include
from .views import *
from django_email_verification import urls as mail_urls


app_name = 'App_auth'

urlpatterns = [
    path('', home, name='home'),
    path('login-or-signup/', login_or_signup, name='login-or-signup'),
    # path('reset/',reset, name='reset'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', logout_view, name='logout'),
    # path('send_email/',sendEmail),
    path('email/',include(mail_urls)),

   
]

