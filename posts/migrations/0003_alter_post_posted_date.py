# Generated by Django 3.2.5 on 2021-11-20 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211120_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now),
        ),
    ]
