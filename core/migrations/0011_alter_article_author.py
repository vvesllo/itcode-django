# Generated by Django 5.0.4 on 2024-05-11 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]
