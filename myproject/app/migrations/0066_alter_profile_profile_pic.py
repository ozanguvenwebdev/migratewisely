# Generated by Django 4.0.3 on 2022-08-24 14:03

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_alter_comment_secondcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=image_optimizer.fields.OptimizedImageField(blank=True, default='/static/assets/images/defaultprofile.jpg', help_text='600x600', null=True, upload_to='profilephotos/', verbose_name="Profil Resmi'"),
        ),
    ]