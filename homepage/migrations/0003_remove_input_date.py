# Generated by Django 5.1.5 on 2025-01-16 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_remove_input_author_alter_input_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='date',
        ),
    ]
