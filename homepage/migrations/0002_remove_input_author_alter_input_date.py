# Generated by Django 5.1.5 on 2025-01-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='author',
        ),
        migrations.AlterField(
            model_name='input',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]