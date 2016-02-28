__author__ = 'Bettina'

from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def current_date(request):
    dt = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': dt})

def hello(request):
    return HttpResponse("Hello World!")

def date_offset(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'date_offset.html', {'offset': offset, 'then_date': dt})
