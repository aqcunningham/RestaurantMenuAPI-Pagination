# Generated by Django 5.0.6 on 2024-07-02 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonAPI', '0008_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
