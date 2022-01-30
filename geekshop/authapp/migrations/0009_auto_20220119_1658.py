# Generated by Django 3.2.9 on 2022-01-19 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20220119_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 13, 58, 15, 668188, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='social_sites',
            field=models.URLField(blank=True, max_length=128, verbose_name='Соц.Сети'),
        ),
    ]