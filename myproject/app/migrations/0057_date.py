# Generated by Django 4.0.3 on 2022-08-21 16:16

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(blank=True, default=app.models.return_date_time, null=True, verbose_name='Comment Date')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date_of_comment', to='app.comment')),
                ('entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date_of_comment', to='app.entry')),
            ],
        ),
    ]