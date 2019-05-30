"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from myapp.views import index1
from cw18.views import render_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', index1),
    path('hw17/', include('hw17.urls')),
    path('hw18/', include('hw18.urls')),
    path('hw19/', include('hw19.urls')),
    path('hw20/', include('hw20.urls')),
    path('hw21/', include('hw21.urls')),
    path('cw19/', include('cw19.urls')),
    path('cw20/', include('cw20.urls')),
    path('render_name/', render_name),
]
