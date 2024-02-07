# Generated by Django 5.0.1 on 2024-02-07 12:30

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
                ('room_name', models.CharField(max_length=32)),
                ('order_game', models.CharField(max_length=50)),
                ('ran_figure', models.CharField(blank=True, max_length=50, null=True)),
                ('ran_four', models.CharField(blank=True, max_length=50, null=True)),
                ('ran_movie', models.CharField(blank=True, max_length=50, null=True)),
                ('ran_music', models.CharField(blank=True, max_length=50, null=True)),
                ('participants', models.IntegerField(default=0)),
            ],
        ),
    ]
