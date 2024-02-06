# Generated by Django 5.0.1 on 2024-02-06 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='영화제목')),
                ('scene', models.TextField(verbose_name='명장면 사진 경로')),
                ('line', models.TextField(verbose_name='명대사')),
            ],
        ),
        migrations.CreateModel(
            name='QuizList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieGames.moviegame')),
            ],
        ),
    ]
