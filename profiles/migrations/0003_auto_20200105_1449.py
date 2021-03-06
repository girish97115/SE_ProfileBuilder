# Generated by Django 3.0.2 on 2020-01-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0002_auto_20200105_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='projects',
        ),
        migrations.AddField(
            model_name='facultyprofile',
            name='articles',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='facultyprofile',
            name='projects',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
