# Generated by Django 5.0.7 on 2024-07-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonAPI', '0002_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.SmallIntegerField(),
        ),
    ]
