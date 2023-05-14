import os
import json
from itertools import chain
from django.core.wsgi import get_wsgi_application
from MainApp.models import Countries, Languages
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoCountries.settings")
application = get_wsgi_application()


with open('countries.json', 'r') as f:
    countries = json.load(f)

# all_countries = [item['country'] for item in countries]
# for country_ in all_countries:
#     country = Countries(name=country_)
#     country.save()
#
# all_languages = [item['languages'] for item in countries]
# languages = sorted(list(set(chain.from_iterable(all_languages))))
# for language_ in languages:
#     language = Languages(name=language_)
#     language.save()

# for item in countries:
#     country = item['country']
#     languages = item['languages']
#     for language in languages:
#         print(country, language)

for item in countries:
    country = Countries.objects.get(name=item['country'])
    for language in item['languages']:
        country.languages.add(Languages.objects.get(name=language))
