# Generated by Django 4.0.3 on 2022-08-24 21:16

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0067_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='default_pic',
            field=image_optimizer.fields.OptimizedImageField(blank=True, default='/static/assets/images/defaultprofile.jpg', help_text='600x600', null=True, upload_to='', verbose_name="Profil Resmi'"),
        ),
    ]
