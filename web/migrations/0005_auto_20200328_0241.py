# Generated by Django 3.0.4 on 2020-03-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]