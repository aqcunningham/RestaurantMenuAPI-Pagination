# Generated by Django 5.0.6 on 2024-07-02 02:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='littlelemonAPI.category'),
        ),
    ]