# Generated by Django 4.0.3 on 2022-09-06 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0078_remove_hottopics_heading_hottopics_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hottopics',
            name='upperHeading',
        ),
    ]
