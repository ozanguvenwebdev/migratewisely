# Generated by Django 4.0.3 on 2022-04-13 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_categories_country_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]