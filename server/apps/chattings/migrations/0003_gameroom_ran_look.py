# Generated by Django 5.0.1 on 2024-02-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chattings', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='ran_look',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]