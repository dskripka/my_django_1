from django.shortcuts import render
from django.http import HttpResponse
from hw19.forms import AddTicketForm

# Create your views here.

def ticket_add(request):
    """
    Создать форму через django forms описывающую заказ авиабилета.
    Форма должна содержать следующие поля - имя, откуда, куда, сколько человек, дата.
    При отправке данных пользователем проверять валидность данных, если они валидны и
    количество человек равно 1 то вывести результат - "стоимость 100$", если количество
    человек больше 1, то стоимость должна считаться по формуле 100*2*количество человек.
    Если данные не валидны, то вывести ошибку.
    """
    if request.method == 'GET':
        context = {'form': AddTicketForm()}
        return render(request, 'ticket_add.html', context)
    elif request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            amount_of_people = data.get('amount_of_people')
            price = 100 if amount_of_people == 1 else 200 * amount_of_people
            data['price'] = price
            context = {'data': data}
            return render(request, 'ticket_details.html', context)
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
