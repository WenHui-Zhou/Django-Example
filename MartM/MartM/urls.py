"""MartM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Login import views as Login_views



urlpatterns = [
    url(r'DataDisp/', Login_views.DataDisp, name='DataDisp'),
    url(r'HomePage/', Login_views.HomePage, name='HomePage'),
    url(r'Apriori/', Login_views.Apriori, name='Apriori'),
    url(r'DrawPai/',Login_views.DrawPai,name = 'DrawPai'),
    url(r'DrawLine/',Login_views.DrawLine,name = 'DrawLine'),
    url(r'DrawHisgram/',Login_views.DrawHisgram,name='DrawHisgram'),
    url(r'^loginCheck/',Login_views.loginCheck,name='loginCheck'),
    url(r'^$',Login_views.FirstPage,name='Login'),
    url(r'^admin/', admin.site.urls),
]
