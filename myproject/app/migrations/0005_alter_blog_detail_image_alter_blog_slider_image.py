# Generated by Django 4.0.3 on 2022-03-16 16:25

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_blog_detail_image_alter_blog_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='detail_image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, help_text='1200x662', null=True, upload_to='blogs/', verbose_name="Detay Sayfa Resmi'"),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slider_image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, help_text='1920x850', null=True, upload_to='blogs/', verbose_name="Slider Resmi'"),
        ),
    ]
