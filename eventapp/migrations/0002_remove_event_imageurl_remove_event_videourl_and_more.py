# Generated by Django 5.0.3 on 2024-03-28 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='imageUrl',
        ),
        migrations.RemoveField(
            model_name='event',
            name='videoUrl',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AddField(
            model_name='event',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='events/videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'mkv'])]),
        ),
    ]