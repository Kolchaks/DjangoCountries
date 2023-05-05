from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json


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
    with open("countries.json", "r") as read_file:
        countries_json = read_file.read()

    for country in countries_json:
        if countries_json['country'] == country:
            context = {
                'country': country
            }
            return render(request, 'countries_list.html', context)


def countries_page(request):
    pass

def languages(request):
    pass