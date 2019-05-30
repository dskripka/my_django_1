from django.shortcuts import render, redirect
from hw20.models import Car


def home(request):
    return render(request, 'hw_20/home.html', context={'cars': Car.objects.all()})

