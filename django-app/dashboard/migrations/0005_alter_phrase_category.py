# Generated by Django 5.1.2 on 2024-11-06 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_phrase_user_phrase_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='phrases', to='dashboard.category'),
            preserve_default=False,
        ),
    ]