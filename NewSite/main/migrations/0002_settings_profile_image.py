# Generated by Django 4.1 on 2022-11-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='profile_image',
            field=models.ImageField(default='profile', upload_to='profile_pics'),
        ),
    ]
