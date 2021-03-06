# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 18:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineBookStore', '0004_auto_20171204_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticsorder',
            name='logistics_token',
            field=models.CharField(default='fkz81NmqEeeXIazgEJ3fJg==', editable=False, max_length=24, verbose_name='物流token'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='deadline',
            field=models.DateTimeField(default=1512471194.4691834, verbose_name='支付期限'),
        ),
        migrations.AlterField(
            model_name='paymentorder',
            name='payment_token',
            field=models.UUIDField(default='fkxgetmqEeeqXqzgEJ3fJg==', editable=False, verbose_name='支付token'),
        ),
        migrations.AlterField(
            model_name='unactivatedaccount',
            name='activation_token',
            field=models.CharField(default='fkwSUtmqEee0PazgEJ3fJg==', editable=False, max_length=24, verbose_name='邮箱验证token'),
        ),
        migrations.AlterField(
            model_name='usedbook',
            name='server_fee',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='服务费'),
        ),
    ]
