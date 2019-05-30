from django.urls import path
from .views import (
    home,
    car_create,
    car_edit,
    car_delete,
)

urlpatterns = [
    path('', home, name='car_home'),
    path('create/', car_create, name='car_create'),
    path('edit/<int:car_id>/', car_edit, name='car_edit'),
    path('delete/<int:car_id>/', car_delete, name='car_delete'),
]
