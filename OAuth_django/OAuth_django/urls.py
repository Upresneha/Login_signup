"""OAuth_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import reset
from distutils.log import log
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from signup.views import signupaction,loginaction,reset
# from login_app.views import loginaction

app_name='signup'
# app_name='login_app'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_auth.urls')),
    # OAuth Path Setup
    path('oauth/', include('social_django.urls', namespace='social')),
    path('signup/',signupaction,name='signup'),
    path('login/',loginaction,name='login'),
    path('verification/', include('verify_email.urls')),
    path('reset/',reset,name='reset')  
    
]  

    


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
