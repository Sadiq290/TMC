# Generated by Django 3.1 on 2021-06-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_profile_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='/static/images/user.png', null=True, upload_to='image/'),
        ),
    ]
