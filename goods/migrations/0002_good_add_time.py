# Generated by Django 3.2.9 on 2021-11-27 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
