# Generated by Django 4.0.3 on 2022-07-16 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_content_country_content_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='slider_image',
        ),
    ]
