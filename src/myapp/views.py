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


def index3(request):
    if request.method == 'POST':
        len_comment = int(len(request.POST.get('comment')))
        comment = (request.POST.get('comment'))

        glas = 'auoieoy'
        sogl = 'qwrtpsdfghjklmnzxcvbnm'
        counter_1 = 0
        counter_2 = 0
        for letter in comment:
            if letter in glas:
                counter_1 += 1
            if letter in sogl:
                counter_2 += 1
        string = f'amount vowels is {counter_1}, amount of sogl is {counter_2}, len is {len_comment}'
        # string = str(len_comment) + ' ' + str(counter_1) + ' ' + str(counter_2)
        return HttpResponse( string )
    return HttpResponse('IT IS GET REQUEST')