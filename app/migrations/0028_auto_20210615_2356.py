# Generated by Django 3.1 on 2021-06-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20210615_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='from_class',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=20),
        ),
        migrations.AlterField(
            model_name='camp',
            name='to_class',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('12+', '12+')], max_length=20),
        ),
    ]
