# Generated by Django 5.1.5 on 2025-01-18 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_input_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hanjaword',
            name='sentence',
        ),
        migrations.RemoveField(
            model_name='output',
            name='hangul',
        ),
        migrations.DeleteModel(
            name='HanjaChar',
        ),
        migrations.DeleteModel(
            name='HanjaWord',
        ),
        migrations.DeleteModel(
            name='Output',
        ),
    ]
