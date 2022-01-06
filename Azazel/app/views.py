import mimetypes
from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def interface(request):
    return render(request,'app/inerface.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'app/home.html')

@login_required(login_url='login')
def panda (request):
    if request.method == 'POST':
        return HttpResponse('http://127.0.0.1:5000/ ')
    return render(request, 'app/panda.html')

@login_required(login_url='login')
def django(request):
    return render(request, 'app/django.html')


@login_required(login_url='login')
def tkinter (request):
    return render(request, 'app/tkinter.html')


@login_required(login_url='login')
def flask (request):
    return render(request, 'app/flask.html')


