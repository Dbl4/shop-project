# Generated by Django 3.2.3 on 2021-07-27 19:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210724_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 29, 19, 40, 52, 528342, tzinfo=utc)),
        ),
    ]