# Generated by Django 3.1 on 2021-06-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_inrank'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='point',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
