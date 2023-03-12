# Generated by Django 4.0.3 on 2022-07-15 13:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_country_expl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_expl', models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama')),
                ('expl', ckeditor.fields.RichTextField(null=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Kullan')),
            ],
            options={
                'verbose_name': 'Sıkça Sorulan Soru',
                'verbose_name_plural': 'SSS',
            },
        ),
    ]
