# Generated by Django 3.1 on 2021-06-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20210615_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Upcoming', 'Upcoming'), ('Held', 'Held')], default='Upcoming', max_length=20),
        ),
    ]
