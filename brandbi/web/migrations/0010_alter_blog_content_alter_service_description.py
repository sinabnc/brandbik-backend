# Generated by Django 5.1 on 2024-12-02 05:47

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_remove_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]