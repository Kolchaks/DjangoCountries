from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from typing import Dict, Any
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

author = {
    "name": "Aleksandr",
    "surname": "Kolchak",
}


def home(request):
    context = {'author': author}
    return render(request, 'index.html', context)


def countries_list(request):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    countries = Country.objects.all()
    paginator = Paginator(countries, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'alphabet': alphabet,
        'page_obj': page_obj,
    }
    return render(request, 'countries-list.html', context)


def languages_list(request):
    languages = Language.objects.all()
    context = { 'languages': languages,}
    return render(request, 'languages-list.html', context)


def country_page(request, country):
    languages = Country.objects.get(name=country).languages.all()
    context = {
        'country': country,
        'languages': languages,
    }
    return render(request, 'country-page.html', context)


def language_page(request, language):
    countries = Country.objects.filter(languages__name=language)
    context = {
        'language': language,
        'countries': countries,
    }
    return render(request, 'language-page.html', context)


def countries_letter(request, letter):
    countries = Country.objects.filter(name__startswith=letter)

    context = {
        'letter': letter,
        'countries': countries,
    }
    return render(request, 'countries-letter.html', context)
