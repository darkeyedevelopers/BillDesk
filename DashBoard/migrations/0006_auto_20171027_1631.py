# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0005_auto_20171027_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rathirohitbill_inven',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='rathirohitbilling',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='rathirohitcustomer',
            options={'managed': False, 'ordering': ['c_name']},
        ),
        migrations.AlterModelOptions(
            name='rathirohitinventory',
            options={'managed': False, 'ordering': ['i_name']},
        ),
    ]
