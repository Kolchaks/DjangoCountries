# Generated by Django 4.2.1 on 2023-05-13 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_rename_country_countries_rename_language_languages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='mame',
            new_name='name',
        ),
    ]
