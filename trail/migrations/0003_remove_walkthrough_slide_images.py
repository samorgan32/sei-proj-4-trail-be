# Generated by Django 3.2.5 on 2021-07-05 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0002_walkthrough_slide_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walkthrough',
            name='slide_images',
        ),
    ]
