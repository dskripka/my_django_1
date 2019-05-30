from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def max_field(request):
    """
    Дана форма с тремя текстовыми полями. Вернуть пользователю максимальное по длине значение поля.
    Пример: введены abc, abcdef, ab - пользователю вернется abcdef.
    Для задания требуется создать новый репозиторий.
    """
    if request.method == 'POST':
        data = request.POST
        field1 = data.get('field1')
        field2 = data.get('field2')
        field3 = data.get('field3')
        dict_ = {len(value): value for value in [field1, field2, field3]}
        max_key = max(dict_.keys())
        return HttpResponse(dict_[max_key])
    return HttpResponse('Waiting for POST request')


def new_year(request):
    """
    Дана форма с одним полем - дата. Если дата первое января - вывести сообщение:
    “С новым {номер года} годом”. В ином случае, вывести дату в формате: год-месяц-день.
    Выполнить задание в репозитории из первого задания.
    """
    if request.method == 'POST':
        date = request.POST.get('date')
        year, month, day= date.split('-')
        if int(month) == int(day) == 1:
            return HttpResponse('Happy New Year!!')
        return HttpResponse(date)
    return HttpResponse('Waiting for POST request')


