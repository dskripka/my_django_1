from django.contrib import admin
from django.urls import path, include
from myapp.views import index1, index2, index3


urlpatterns = [
    path('index1/', index1),
    path('index2/', index2),
    path('index3/', index3),
    ]