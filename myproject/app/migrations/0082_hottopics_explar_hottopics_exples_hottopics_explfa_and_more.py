# Generated by Django 4.0.3 on 2022-09-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0081_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='hottopics',
            name='explAr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Ar'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='explEs',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Es'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='explFa',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Fa'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='explFr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Fr'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='explHi',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Hi'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='explTr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Tr'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='explUr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Ur'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='explVi',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Vi'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplAr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Ar'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplEs',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Es'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplFa',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Fa'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplFr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Fr'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplHi',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Hi'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplTr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Tr'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplUr',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Ur'),
        ),
        migrations.AddField(
            model_name='hottopics',
            name='upperExplVi',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü Vi'),
        ),
        migrations.AlterField(
            model_name='hottopics',
            name='expl',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama En'),
        ),
        migrations.AlterField(
            model_name='hottopics',
            name='upperExpl',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama Üstü En'),
        ),
    ]