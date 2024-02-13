# Generated by Django 5.0.1 on 2024-02-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=32, unique=True)),
                ('order_game', models.CharField(max_length=50)),
                ('order_num', models.CharField(blank=True, max_length=10, null=True)),
                ('ran_figure', models.CharField(blank=True, max_length=50, null=True)),
                ('ran_four', models.CharField(blank=True, max_length=50, null=True)),
                ('ran_movie', models.CharField(blank=True, max_length=50, null=True)),
                ('ran_music', models.CharField(blank=True, max_length=50, null=True)),
                ('ran_look', models.CharField(blank=True, max_length=50, null=True)),
                ('participants', models.IntegerField(default=0)),
            ],
        ),
    ]
