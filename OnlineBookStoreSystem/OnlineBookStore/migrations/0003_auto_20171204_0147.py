# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineBookStore', '0002_auto_20171203_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.TextField(default='', verbose_name='消息标题'),
        ),
        migrations.AlterField(
            model_name='logisticsorder',
            name='logistics_token',
            field=models.CharField(default='BOfhothSEeepdKzgEJ3fJg==', editable=False, max_length=24, verbose_name='物流token'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='deadline',
            field=models.DateTimeField(default=1512323243.928278, verbose_name='支付期限'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='payment_token',
            field=models.UUIDField(default='BOdsXNhSEee5zqzgEJ3fJg==', editable=False, verbose_name='支付token'),
        ),
        migrations.AlterField(
            model_name='unactivatedaccount',
            name='activation_token',
            field=models.CharField(default='BOceMNhSEeeEK6zgEJ3fJg==', editable=False, max_length=24, verbose_name='邮箱验证token'),
        ),
    ]
