# Generated by Django 5.0.6 on 2024-05-13 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_mainmodel_video_alter_mainmodel_voice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MainModel',
            new_name='Post',
        ),
    ]
