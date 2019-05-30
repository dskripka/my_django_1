from django.shortcuts import render, redirect
from hw20.models import Car
from hw20.forms import CarForm
from django.http import HttpResponse


def car_create(request):
    if request.method == 'GET':
        return render(request, 'hw_20/create.html', context={'form': CarForm()})
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Car.objects.create(
                brand=data.get('brand'),
                model=data.get('model'),
                color=data.get('color'),
                weight=data.get('weight'),
                owner_full_name=data.get('owner_full_name'),
                year_issue=data.get('year_issue'),
            )
            return redirect('car_home')
        else:
            return HttpResponse(f'{form.errors}')
    return HttpResponse('INVALID REQUEST METHOD')
