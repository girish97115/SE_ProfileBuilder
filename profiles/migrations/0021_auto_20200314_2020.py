# Generated by Django 3.0.2 on 2020-03-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0020_auto_20200313_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='accepted',
            field=models.IntegerField(default=-1),
        ),
    ]