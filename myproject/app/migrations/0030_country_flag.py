# Generated by Django 4.0.3 on 2022-07-16 10:43

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_quickinfo_options_alter_country_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=image_optimizer.fields.OptimizedImageField(blank=True, help_text='kare', null=True, upload_to='blogs/', verbose_name="Ülke bayrağı'"),
        ),
    ]
