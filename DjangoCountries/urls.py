"""
URL configuration for DjangoCountries project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('countries/', views.countries_list, name='countries'),
    path('countries/letter/<country>/', views.country_page, name='country-name'),
    path('countries/<letter>/', views.countries_letter, name='countries-letter'),
    path('languages/', views.languages_list, name='languages'),
    path('languages/<language>/', views.language_page, name='language-name'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

