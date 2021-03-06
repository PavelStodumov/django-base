# Generated by Django 3.2.9 on 2022-01-19 13:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20220119_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='social_sites',
            field=models.CharField(blank=True, max_length=128, verbose_name='Соц.Сети'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 13, 52, 18, 8623, tzinfo=utc)),
        ),
    ]
