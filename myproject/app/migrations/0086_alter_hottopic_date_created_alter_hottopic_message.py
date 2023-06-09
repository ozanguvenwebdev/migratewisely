# Generated by Django 4.0.3 on 2022-09-19 15:03

import app.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0085_hottopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hottopic',
            name='date_created',
            field=models.DateTimeField(blank=True, default=app.models.return_date_time, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='hottopic',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
