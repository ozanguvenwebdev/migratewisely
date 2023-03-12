# Generated by Django 4.0.3 on 2022-04-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_category_status_country_status_tag_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='popular',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Popüler Kategori mi?'),
        ),
        migrations.AddField(
            model_name='tag',
            name='popular',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Popüler Etiket mi?'),
        ),
    ]