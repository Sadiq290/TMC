# Generated by Django 3.1 on 2021-06-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_campparticipant_camper_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='from_class',
            field=models.CharField(default='1', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp',
            name='to_class',
            field=models.CharField(default='10', max_length=20),
            preserve_default=False,
        ),
    ]