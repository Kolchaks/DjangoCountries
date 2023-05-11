from typing import Dict, Any
from django.shortcuts import render, HttpResponse
import json
from itertools import chain

# Create your views here.

author = {
    "name": "Aleksandr",
    "surname": "Kolchak",
}

with open('countries.json', 'r') as f:
    countries = json.load(f)


def home(request):
    context = {'author': author}
    return render(request, 'index.html', context)


def countries_list(request):
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def country_page(request, country):
    for item in countries:
        if item['country'] == country:
            languages = item['languages']
            context = {'country': country,
                       'languages': languages,
                       }
    return render(request, 'country-page.html', context)


def list_of_languages(request):
    all_languages = [item['languages'] for item in countries]
    languages = sorted(list(set(chain.from_iterable(all_languages))))
    context = {'languages': languages}

    return render(request, 'languages-list.html', context)
