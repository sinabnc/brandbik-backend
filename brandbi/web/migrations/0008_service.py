# Generated by Django 5.1 on 2024-11-29 08:48

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='service_images/')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='service_icons/')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_description', models.TextField()),
                ('alt_text', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ('date_added',),
            },
        ),
    ]