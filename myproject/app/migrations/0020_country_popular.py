# Generated by Django 4.0.3 on 2022-04-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_category_popular_tag_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='popular',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Popüler Ülke mi?'),
        ),
    ]
