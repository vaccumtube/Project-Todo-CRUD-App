# Generated by Django 5.0.6 on 2024-05-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoapp',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
