# Generated by Django 3.2.9 on 2022-01-16 10:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20220112_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 10, 9, 21, 200244, tzinfo=utc)),
        ),
    ]
