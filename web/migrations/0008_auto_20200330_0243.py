# Generated by Django 3.0.4 on 2020-03-29 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0007_auto_20200329_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='madarrrrr',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Madar_Kharj', to='web.Person'),
        ),
        migrations.AddField(
            model_name='expense',
            name='member',
            field=models.ManyToManyField(related_name='person2person', to='web.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='MadarKharj',
        ),
    ]
