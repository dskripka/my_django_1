from django.shortcuts import redirect
from hw20.models import Car


def car_delete(request, car_id):
    Car.objects.get(id=car_id).delete()
    return redirect('car_home')
