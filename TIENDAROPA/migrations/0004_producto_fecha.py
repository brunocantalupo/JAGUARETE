# Generated by Django 3.2.4 on 2021-07-03 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDAROPA', '0003_auto_20210703_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
