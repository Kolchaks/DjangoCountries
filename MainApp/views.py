from typing import Dict, Any
from django.shortcuts import render, HttpResponse
import json
from MainApp.models import Countries, Languages

author = {
    "name": "Aleksandr",
    "surname": "Kolchak",
}


# with open('countries.json', 'r') as f:
#     countries = json.load(f)


def home(request):
    context = {'author': author}
    return render(request, 'index.html', context)


def countries_list(request):
    countries = Countries.objects.all()
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def languages_list(request):
    languages = Languages.objects.all()
    context = {'languages': languages}
    return render(request, 'languages-list.html', context)


def country_page(request, country):
    country_name = Countries.objects.get(name=country)
    languages = country_name.languages.all()
    context = {
        'country': country_name.name,
        'languages': languages,
    }
    return render(request, 'country-page.html', context)

# def language_page(request, language):
#     language_name = Languages.objects.get(name=language)
#     country = Countries.objects.get(name=country)
#     countries_ = country.languages.get(language_name)
#
#     context = {
#         'language': language_name.name,
#         'countries': countries_,
#     }
#     return render(request, 'language-page.html', context)
