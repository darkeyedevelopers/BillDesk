# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 09:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0021_auto_20171028_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='SAMRBill_Inven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SAMRBilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saletime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tot_price', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SAMRCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('c_name', models.CharField(max_length=100)),
                ('age_group', models.IntegerField()),
                ('village', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('gst_in', models.CharField(default=b'', max_length=15)),
                ('del_flag', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['c_name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SAMRInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('i_name', models.CharField(max_length=100)),
                ('i_price', models.IntegerField(default=0)),
                ('gst_perc', models.IntegerField(default=0)),
                ('del_flag', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['i_name'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='samrbilling',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_id', to='DashBoard.SAMRCustomer'),
        ),
        migrations.AddField(
            model_name='samrbill_inven',
            name='Billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.SAMRBilling'),
        ),
        migrations.AddField(
            model_name='samrbill_inven',
            name='Inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.SAMRInventory'),
        ),
    ]
