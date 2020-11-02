"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('collab/',collaboration),
    path('get/',getroom),
    path('meeting/',meeting),
    #path('create/',create),
    path('delete/',deletegroup),
    path('create2/',postroom),
    path('team/',team_members),
    path('leads/',leads),
    path('del2/<int:id>/',getid),
    path('networking/',networking),
    path('dnac/',dnac_login),
    path('get_device/',network_device_list),
    path('Network_health/',Network_health),
]
