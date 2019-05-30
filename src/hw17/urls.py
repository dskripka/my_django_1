from django.urls import path
from hw17.views import (
    max_field,
    new_year,
)

urlpatterns = [
    path('max_field/', max_field),
    path('new_year/', new_year),
]
