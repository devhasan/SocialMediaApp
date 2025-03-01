# Generated by Django 5.1.5 on 2025-02-21 08:40

import blog.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image_alter_post_publish_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.blog_directory_name),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Publish', 'publish'), ('Unpublish', 'unpublish')], default='published', max_length=16),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
