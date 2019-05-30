# Создать форму из трех полей: имя, фамилия, возраст. Создать представление(view).
# В случае get запроса отображать форму. В случае post запроса записывать все
# три поля в виде 1 строки в файл и после отображать форму.


from django.shortcuts import render
from django.http import HttpResponse

FILE_NAME = 'write_line.txt'


def write_line(request):
    if request.method == 'GET':
        return render(request, 'write_line_form.html')
    elif request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        with open(FILE_NAME, 'a') as my_file:
            my_file.write(f'{firstname} {lastname} {age}\n')
        return render(request, 'write_line_form.html')
    return HttpResponse('NOT SUPPORTED METHOD')

def display_lines(request):
    if request.method == 'GET':
        with open(FILE_NAME) as my_file:
            lines = my_file.readlines()
        return render(request, 'display_lines.html', {'lines': lines})
    return HttpResponse('NOT SUPPORTED METHOD')

def clear_file(request):
    if request.method == 'GET':
        with open(FILE_NAME, 'w'):
            pass
        return render(request, 'write_line_form.html')
    return HttpResponse('NOT SUPPORTED METHOD')
