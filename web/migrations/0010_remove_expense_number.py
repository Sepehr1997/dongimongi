# Generated by Django 3.0.4 on 2020-03-30 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_person_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='number',
        ),
    ]
