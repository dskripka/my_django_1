from django.urls import path
from hw19.views import ticket_add

urlpatterns = [
    path('add/', ticket_add, name='ticket_add'),
]
