# Generated by Django 4.0.3 on 2022-08-22 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_remove_category_comments_remove_category_entries_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_of_comment', to='app.comment'),
        ),
    ]
