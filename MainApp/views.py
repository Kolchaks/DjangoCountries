from typing import Dict, Any
from django.shortcuts import render, HttpResponse
import json
from MainApp.models import Countries, Languages

author = {
    "name": "Aleksandr",
    "surname": "Kolchak",
}


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
    country = Countries.objects.get(name=country)
    languages = country.languages.all()
    context = {
        'country': country.name,
        'languages': languages,
    }
    return render(request, 'country-page.html', context)


def language_page(request, language):
    countries = Countries.objects.filter(name='language')
    context = {
        'language': language,
        'countries': countries,
    }
    return render(request, 'language-page.html', context)
