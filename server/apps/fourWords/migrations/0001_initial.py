# Generated by Django 5.0.1 on 2024-02-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Four',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two', models.CharField(blank=True, max_length=20, null=True)),
                ('answer', models.CharField(max_length=20)),
            ],
        ),
    ]
