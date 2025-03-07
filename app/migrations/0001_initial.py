# Generated by Django 5.0.6 on 2024-05-13 05:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(upload_to='media/photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'heic'])])),
                ('voice', models.FileField(upload_to='photos/audios')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
