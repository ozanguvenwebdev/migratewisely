# Generated by Django 4.0.3 on 2022-07-26 18:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_alter_category_expl_alter_category_exples_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='descriptionAr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Ar'),
        ),
        migrations.AddField(
            model_name='category',
            name='descriptionFa',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Fa'),
        ),
        migrations.AddField(
            model_name='category',
            name='descriptionUr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Ur'),
        ),
        migrations.AddField(
            model_name='category',
            name='explAr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Ar'),
        ),
        migrations.AddField(
            model_name='category',
            name='explFa',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Fa'),
        ),
        migrations.AddField(
            model_name='category',
            name='explUr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama Ur'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywordsAr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Ar'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywordsFa',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Fa'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywordsUr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Ur'),
        ),
        migrations.AddField(
            model_name='category',
            name='nameAr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Kategori Adı Ar'),
        ),
        migrations.AddField(
            model_name='category',
            name='nameFa',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Kategori Adı Fa'),
        ),
        migrations.AddField(
            model_name='category',
            name='nameUr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Kategori Adı Ur'),
        ),
        migrations.AddField(
            model_name='content',
            name='descriptionAr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması Ar', null=True, verbose_name='Google SEO Description Ar'),
        ),
        migrations.AddField(
            model_name='content',
            name='descriptionFa',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması Fa', null=True, verbose_name='Google SEO Description Fa'),
        ),
        migrations.AddField(
            model_name='content',
            name='descriptionUr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması Ur', null=True, verbose_name='Google SEO Description Ur'),
        ),
        migrations.AddField(
            model_name='content',
            name='explAr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Keywords Ar'),
        ),
        migrations.AddField(
            model_name='content',
            name='explFa',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Keywords Fa'),
        ),
        migrations.AddField(
            model_name='content',
            name='explUr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Keywords Ur'),
        ),
        migrations.AddField(
            model_name='content',
            name='headerAr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Başlık Ar'),
        ),
        migrations.AddField(
            model_name='content',
            name='headerFa',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Başlık Fa'),
        ),
        migrations.AddField(
            model_name='content',
            name='headerUr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Başlık Ur'),
        ),
        migrations.AddField(
            model_name='content',
            name='keywordsAr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Ar', null=True, verbose_name='Keywords Ar'),
        ),
        migrations.AddField(
            model_name='content',
            name='keywordsFa',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Fa', null=True, verbose_name='Keywords Fa'),
        ),
        migrations.AddField(
            model_name='content',
            name='keywordsUr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın Ur', null=True, verbose_name='Keywords Ur'),
        ),
        migrations.AddField(
            model_name='content',
            name='short_explAr',
            field=models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama Ar'),
        ),
        migrations.AddField(
            model_name='content',
            name='short_explFa',
            field=models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama Fa'),
        ),
        migrations.AddField(
            model_name='content',
            name='short_explUr',
            field=models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama Ur'),
        ),
        migrations.AddField(
            model_name='continent',
            name='nameAr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Kıta Adı Ar'),
        ),
        migrations.AddField(
            model_name='continent',
            name='nameFa',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Kıta Adı Fa'),
        ),
        migrations.AddField(
            model_name='continent',
            name='nameUr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Kıta Adı Ur'),
        ),
        migrations.AddField(
            model_name='country',
            name='descriptionAr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Ar'),
        ),
        migrations.AddField(
            model_name='country',
            name='descriptionFa',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Fa'),
        ),
        migrations.AddField(
            model_name='country',
            name='descriptionUr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Ur'),
        ),
        migrations.AddField(
            model_name='country',
            name='explAr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Ülke Adı Ar'),
        ),
        migrations.AddField(
            model_name='country',
            name='explFa',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Ülke Adı Fa'),
        ),
        migrations.AddField(
            model_name='country',
            name='explUr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Ülke Adı Ur'),
        ),
        migrations.AddField(
            model_name='country',
            name='keywordsAr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Ar'),
        ),
        migrations.AddField(
            model_name='country',
            name='keywordsFa',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Fa'),
        ),
        migrations.AddField(
            model_name='country',
            name='keywordsUr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Ur'),
        ),
        migrations.AddField(
            model_name='country',
            name='nameAr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ülke Adı Ar'),
        ),
        migrations.AddField(
            model_name='country',
            name='nameFa',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ülke Adı Fa'),
        ),
        migrations.AddField(
            model_name='country',
            name='nameUr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ülke Adı Ur'),
        ),
        migrations.AddField(
            model_name='navigation',
            name='nameAr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Başlık Ar'),
        ),
        migrations.AddField(
            model_name='navigation',
            name='nameFa',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Başlık Fa'),
        ),
        migrations.AddField(
            model_name='navigation',
            name='nameUr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Başlık Ur'),
        ),
        migrations.AddField(
            model_name='quickinfo',
            name='short_explAr',
            field=models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama Ar'),
        ),
        migrations.AddField(
            model_name='quickinfo',
            name='short_explFa',
            field=models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama Fa'),
        ),
        migrations.AddField(
            model_name='quickinfo',
            name='short_explUr',
            field=models.TextField(blank=True, null=True, verbose_name='Kısa Açıklama Ur'),
        ),
        migrations.AddField(
            model_name='tag',
            name='descriptionAr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Ar'),
        ),
        migrations.AddField(
            model_name='tag',
            name='descriptionFa',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Fa'),
        ),
        migrations.AddField(
            model_name='tag',
            name='descriptionUr',
            field=models.TextField(blank=True, help_text='max 160 karakterli bir seo açıklaması', null=True, verbose_name='Google SEO Description Ur'),
        ),
        migrations.AddField(
            model_name='tag',
            name='keywordsAr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Ar'),
        ),
        migrations.AddField(
            model_name='tag',
            name='keywordsFa',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Fa'),
        ),
        migrations.AddField(
            model_name='tag',
            name='keywordsUr',
            field=models.TextField(blank=True, help_text='5 ila 10 tane anahtar kelimeyi aralarına virgül koyarak yazacaksın', null=True, verbose_name='Keywords Ur'),
        ),
        migrations.AddField(
            model_name='tag',
            name='nameAr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Etiket Adı Ar'),
        ),
        migrations.AddField(
            model_name='tag',
            name='nameFa',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Etiket Adı Fa'),
        ),
        migrations.AddField(
            model_name='tag',
            name='nameUr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Etiket Adı Ur'),
        ),
    ]
