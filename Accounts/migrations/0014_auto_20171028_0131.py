# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0013_profile_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='store_id',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
