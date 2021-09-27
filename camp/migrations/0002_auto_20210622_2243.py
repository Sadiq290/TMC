# Generated by Django 3.1 on 2021-06-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='banner',
            field=models.ImageField(upload_to='camp/banners/'),
        ),
        migrations.AlterField(
            model_name='camp',
            name='camp_logo',
            field=models.ImageField(upload_to='camp/logos/'),
        ),
        migrations.AlterField(
            model_name='camporganizer',
            name='image',
            field=models.ImageField(default='/user.png', upload_to='camp/camp_organizer/'),
        ),
        migrations.AlterField(
            model_name='camptrainer',
            name='image',
            field=models.ImageField(default='/user.png', upload_to='camp/camp_trainers/'),
        ),
    ]