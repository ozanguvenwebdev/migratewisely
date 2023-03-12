# Generated by Django 4.0.3 on 2022-07-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_content_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description'),
        ),
        migrations.AddField(
            model_name='country',
            name='keywords',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description'),
        ),
        migrations.AddField(
            model_name='tag',
            name='keywords',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords'),
        ),
    ]
