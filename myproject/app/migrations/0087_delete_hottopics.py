# Generated by Django 4.0.3 on 2022-09-19 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0086_alter_hottopic_date_created_alter_hottopic_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HotTopics',
        ),
    ]
