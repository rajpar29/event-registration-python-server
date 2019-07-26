# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-07 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20180101_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_code',
            field=models.CharField(help_text='Event Code', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='registration_no',
            field=models.CharField(help_text='Registration Number', max_length=100, unique=True),
        ),
    ]
