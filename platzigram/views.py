from django.urls import path
from django.http import HttpResponse
import json


# Utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh hi current time server is!!{str(now)}')


def hi(request):
    # https://docs.djangoproject.com/en/3.1/ref/request-response/
    print(request.scheme)
    print(request.body)
    print(request.path)
    print(request.path_info)
    print(request.method)
    print(request.GET)
    print(request.POST)
    # print(request.META) # Those are the headers of request
    return HttpResponse('Hii!!')

# return a group of numbers sorted
def challenge_numbers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')] 
    numbers = sorted(numbers)
    data = {
        'status':'ok',
        'data': numbers
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    greets = f'Hola {name} tu edad es {age}'
    return HttpResponse(greets)