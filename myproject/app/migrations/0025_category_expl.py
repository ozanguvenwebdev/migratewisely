# Generated by Django 4.0.3 on 2022-04-18 14:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_continent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='expl',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
