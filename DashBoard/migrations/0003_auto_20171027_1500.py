# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0002_auto_20171020_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='rathirohitBill_Inven',
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
            name='rathirohitBilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saletime', models.DateTimeField(auto_now_add=True)),
                ('tot_price', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='rathirohitCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('c_name', models.CharField(max_length=100)),
                ('age_group', models.IntegerField()),
                ('village', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('gst_in', models.CharField(default=None, max_length=15)),
                ('del_flag', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['c_name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='rathirohitInventory',
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
            model_name='rathirohitbilling',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.rathirohitCustomer'),
        ),
        migrations.AddField(
            model_name='rathirohitbill_inven',
            name='Billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.rathirohitBilling'),
        ),
        migrations.AddField(
            model_name='rathirohitbill_inven',
            name='Inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.rathirohitInventory'),
        ),
    ]
