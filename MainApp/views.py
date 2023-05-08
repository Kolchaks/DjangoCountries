from django.shortcuts import render, HttpResponse
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


def country_page(request, country):
    # for item in countries:
    #     if item['country'] in countries:
    context = {'country': country}

    return render(request, 'country-page.html', context)
