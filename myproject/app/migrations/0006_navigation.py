# Generated by Django 4.0.3 on 2022-03-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_blog_detail_image_alter_blog_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Başlık')),
                ('url_name', models.SlugField(blank=True, help_text='This will be filled automatically', max_length=500, verbose_name='Sayfa Uzantısı')),
                ('status', models.BooleanField(blank=True, default=True, null=True, verbose_name='Kullan')),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Navigasyon',
                'verbose_name_plural': 'Navigasyonlar',
            },
        ),
    ]
