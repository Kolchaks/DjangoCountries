# Generated by Django 4.2.1 on 2023-05-19 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_countries_languages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Countries',
            new_name='Country',
        ),
        migrations.RenameModel(
            old_name='Languages',
            new_name='Language',
        ),
    ]
