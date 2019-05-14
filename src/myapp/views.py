from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index1(request):
    name = request.POST.get('name')
    return HttpResponse('len is {}'.format(len(name)))


def index2(request):
    age = int(request.POST.get('age'))
    if age < 18:
        return HttpResponse('Error')
    return HttpResponse('Welcome')

