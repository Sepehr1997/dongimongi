# Generated by Django 3.0.4 on 2020-04-01 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_expense_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='user',
        ),
    ]
