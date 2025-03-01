# Generated by Django 5.1.5 on 2025-02-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_description_alter_post_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('unpublish', 'Unpublish')], default='published', max_length=16),
        ),
    ]
