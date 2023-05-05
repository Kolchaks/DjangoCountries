from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json
from DjangoCountries import countriess.json

# Create your views here.

author = {
    "name": "Aleksandr",
    "surname": "Kolchak",
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

def countries_list(request):
    pass

def countries_page(request):
    pass

def languages(request):
    pass