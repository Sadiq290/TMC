# Generated by Django 3.1 on 2021-06-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210602_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='point',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='answer',
            field=models.FloatField(),
        ),
    ]