# Generated by Django 4.0.3 on 2022-07-25 09:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_category_descriptiones_category_descriptionfr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='expl',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='category',
            name='explEs',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Es'),
        ),
        migrations.AlterField(
            model_name='category',
            name='explFr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Fr'),
        ),
        migrations.AlterField(
            model_name='category',
            name='explHi',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Hi'),
        ),
        migrations.AlterField(
            model_name='category',
            name='explTr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Tr'),
        ),
        migrations.AlterField(
            model_name='category',
            name='explVi',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Vi'),
        ),
    ]
