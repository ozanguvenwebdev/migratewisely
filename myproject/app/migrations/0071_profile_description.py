# Generated by Django 4.0.3 on 2022-08-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0070_alter_country_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Profile Description'),
        ),
    ]
