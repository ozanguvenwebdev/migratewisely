# Generated by Django 4.0.3 on 2022-09-06 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0079_remove_hottopics_upperheading'),
    ]

    operations = [
        migrations.AddField(
            model_name='hottopics',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_of_hottopics', to='app.content'),
        ),
    ]