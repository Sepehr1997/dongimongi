# Generated by Django 3.0.4 on 2020-03-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
