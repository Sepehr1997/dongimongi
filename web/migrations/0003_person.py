# Generated by Django 3.0.4 on 2020-03-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_expense_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sahm', models.IntegerField()),
            ],
        ),
    ]
