# Generated by Django 5.0.1 on 2024-02-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicGame_2000',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='노래제목')),
                ('music', models.TextField(verbose_name='노래 파일 경로')),
                ('singer', models.CharField(max_length=20, verbose_name='가수')),
                ('youtube', models.TextField(verbose_name='유튜브')),
            ],
        ),
        migrations.CreateModel(
            name='MusicGame_2010',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='노래제목')),
                ('music', models.TextField(verbose_name='노래 파일 경로')),
                ('singer', models.CharField(max_length=20, verbose_name='가수')),
                ('youtube', models.TextField(verbose_name='유튜브')),
            ],
        ),
        migrations.CreateModel(
            name='MusicGame_2020',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='노래제목')),
                ('music', models.TextField(verbose_name='노래 파일 경로')),
                ('singer', models.CharField(max_length=20, verbose_name='가수')),
                ('youtube', models.TextField(verbose_name='유튜브')),
            ],
        ),
    ]
