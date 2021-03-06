# Generated by Django 3.2.4 on 2021-07-01 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Walkthrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('cover_slide', models.ImageField(default='images/default.jpeg', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walkthrough', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('image', models.ImageField(default='images/default.jpeg', upload_to='images/')),
                ('description', models.TextField()),
                ('walkthrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='trail.walkthrough')),
            ],
            options={
                'verbose_name_plural': 'slides',
                'ordering': ['position'],
            },
        ),
    ]
