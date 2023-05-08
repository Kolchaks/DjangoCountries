from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json

# Create your views here.

author = {
    "name": "Aleksandr",
    "surname": "Kolchak",
}

with open('countries.json', 'r') as read_file:
    countries = json.load(read_file)


def home(request):
    context = {"name": 'Хватит лениться!'}
    return render(request, 'index.html', context)


def about(request):
    context = {'author': author}
    return render(request, 'about.html', context)


def countries_list(request):
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def countries_page(request):
    pass


def languages(request):
    pass
