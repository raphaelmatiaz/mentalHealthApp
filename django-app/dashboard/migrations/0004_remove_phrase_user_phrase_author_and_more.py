# Generated by Django 5.1.2 on 2024-11-05 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_category_rename_text_phrase_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phrase',
            name='user',
        ),
        migrations.AddField(
            model_name='phrase',
            name='author',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='phrase',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phrases', to='dashboard.category'),
        ),
    ]