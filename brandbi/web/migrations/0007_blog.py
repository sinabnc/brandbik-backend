# Generated by Django 5.1 on 2024-11-29 08:21

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('date', models.DateField(auto_now_add=True)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_description', models.TextField()),
                ('alt_text', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ('date',),
            },
        ),
    ]
