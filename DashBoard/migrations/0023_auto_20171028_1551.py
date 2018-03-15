# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0022_auto_20171028_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestbill_inven',
            name='Billing',
        ),
        migrations.RemoveField(
            model_name='guestbill_inven',
            name='Inventory',
        ),
        migrations.RemoveField(
            model_name='guestbilling',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='onk_rbill_inven',
            name='Billing',
        ),
        migrations.RemoveField(
            model_name='onk_rbill_inven',
            name='Inventory',
        ),
        migrations.RemoveField(
            model_name='onk_rbilling',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='qwertybill_inven',
            name='Billing',
        ),
        migrations.RemoveField(
            model_name='qwertybill_inven',
            name='Inventory',
        ),
        migrations.RemoveField(
            model_name='qwertybilling',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='samrbill_inven',
            name='Billing',
        ),
        migrations.RemoveField(
            model_name='samrbill_inven',
            name='Inventory',
        ),
        migrations.RemoveField(
            model_name='samrbilling',
            name='Customer',
        ),
        migrations.AlterField(
            model_name='rathirohitbilling',
            name='Customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashBoard.rathirohitCustomer'),
        ),
        migrations.DeleteModel(
            name='guestBill_Inven',
        ),
        migrations.DeleteModel(
            name='guestBilling',
        ),
        migrations.DeleteModel(
            name='guestCustomer',
        ),
        migrations.DeleteModel(
            name='guestInventory',
        ),
        migrations.DeleteModel(
            name='onk_rBill_Inven',
        ),
        migrations.DeleteModel(
            name='onk_rBilling',
        ),
        migrations.DeleteModel(
            name='onk_rCustomer',
        ),
        migrations.DeleteModel(
            name='onk_rInventory',
        ),
        migrations.DeleteModel(
            name='QWERTYBill_Inven',
        ),
        migrations.DeleteModel(
            name='QWERTYBilling',
        ),
        migrations.DeleteModel(
            name='QWERTYCustomer',
        ),
        migrations.DeleteModel(
            name='QWERTYInventory',
        ),
        migrations.DeleteModel(
            name='SAMRBill_Inven',
        ),
        migrations.DeleteModel(
            name='SAMRBilling',
        ),
        migrations.DeleteModel(
            name='SAMRCustomer',
        ),
        migrations.DeleteModel(
            name='SAMRInventory',
        ),
    ]
