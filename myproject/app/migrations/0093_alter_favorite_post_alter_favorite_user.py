# Generated by Django 4.0.3 on 2022-09-29 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0092_alter_favorite_post_alter_favorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_of_favorite', to='app.content'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
