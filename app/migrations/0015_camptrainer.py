# Generated by Django 3.1 on 2021-06-14 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210613_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampTrainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('institutuion', models.CharField(max_length=1000)),
                ('work', models.CharField(max_length=1000)),
                ('image', models.ImageField(default='/user.png', upload_to='camp_trainers/')),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainers', to='app.camp')),
            ],
        ),
    ]
