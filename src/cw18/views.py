from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def render_name(request):
    if request.method == 'GET':
        template = loader.get_template('form_name.html')
        return HttpResponse(template.render({}, request))
    if request.method == 'POST':
        name = request.POST.get('name')
        template = loader.get_template('display_name.html')
        return HttpResponse(template.render({'name': name}, request))
