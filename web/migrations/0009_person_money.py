# Generated by Django 3.0.4 on 2020-03-30 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20200330_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='money',
            field=models.BigIntegerField(default=0),
        ),
    ]
