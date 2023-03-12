# Generated by Django 4.0.3 on 2022-07-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_rename_faq_quickinfo_alter_quickinfo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quickinfo',
            options={'verbose_name': 'Anasayfa Kutu', 'verbose_name_plural': 'Anasayfa Kutular'},
        ),
        migrations.AlterField(
            model_name='country',
            name='popular',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Popüler Ülke mi?'),
        ),
    ]