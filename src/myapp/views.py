from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        return HttpResponse('len is {}'.format(len(name)))
    return HttpResponse('It is GET request')
