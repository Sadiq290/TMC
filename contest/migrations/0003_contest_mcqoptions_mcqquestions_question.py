# Generated by Django 3.1 on 2021-06-27 17:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest', '0002_auto_20210627_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('type', models.CharField(choices=[('Pre Registered', 'Pre Registered'), ('On Spot', 'On Spot')], max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('date', models.CharField(max_length=1000)),
                ('organizer', models.CharField(max_length=2000)),
                ('code', models.CharField(max_length=30)),
                ('description', ckeditor.fields.RichTextField()),
                ('total_questions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000)),
                ('answer', models.CharField(max_length=1000)),
                ('index', models.IntegerField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='contest.contest')),
            ],
        ),
        migrations.CreateModel(
            name='MCQQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000)),
                ('index', models.IntegerField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcq_questions', to='contest.contest')),
            ],
        ),
        migrations.CreateModel(
            name='MCQOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=2000)),
                ('index', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='contest.mcqquestions')),
            ],
        ),
    ]