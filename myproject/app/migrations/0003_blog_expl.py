# Generated by Django 4.0.3 on 2022-03-16 16:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blog_detail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='expl',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
