from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

author = {
    "name": "Aleksandr",
    "surname": "Kolchak",
    "phone": "+7 999 777 55 33",
    "email": "ondatr@gmail.com",
}

def home(request):
    context = {
        "name": author['name'],
        "surname": author['surname']
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'author': author
    }
    return render(request, 'about.html', context)