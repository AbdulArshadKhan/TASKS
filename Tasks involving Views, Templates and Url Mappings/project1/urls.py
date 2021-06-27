"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1 import views
urlpatterns = [     
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht',views.ht),
    path('hp/<str:uname>',views.par1),
    path('ren',views.ren),
    path('rend',views.rend),
    path('bif/<str:name>/<int:age>',views.bif),
    path('form/',views.form),
    path('form/html/result.html',views.result),
    path('task1',views.task1),
    # path('data',views.data),
    # path('data1',views.data1)
]
