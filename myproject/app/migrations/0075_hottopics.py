# Generated by Django 4.0.3 on 2022-09-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0074_alter_expirecode_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upperHeading', models.CharField(blank=True, max_length=200, null=True, verbose_name='Üst Başlık')),
                ('heading', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık')),
                ('upperExpl', models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü')),
                ('expl', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
            ],
        ),
    ]