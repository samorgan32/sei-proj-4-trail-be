# Generated by Django 3.2.4 on 2021-06-30 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walkthrough',
            old_name='creator',
            new_name='owner',
        ),
    ]
