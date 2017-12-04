# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 17:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('mail', models.EmailField(default='', max_length=254, unique=True, verbose_name='邮箱地址')),
                ('password', models.CharField(default='', max_length=36, verbose_name='密码')),
                ('address', models.CharField(default='', max_length=255, verbose_name='家庭住址')),
                ('balance', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='余额（分）')),
                ('type', models.IntegerField(choices=[(0, '平台管理员'), (1, '运送代理商'), (2, '普通用户')], default=2, verbose_name='用户类型代码')),
                ('trolley', models.TextField(default='', editable=False, verbose_name='购物车信息')),
            ],
            options={
                'verbose_name': '账号',
                'db_table': 'Account',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('title', models.TextField(default='', verbose_name='标题')),
                ('author', models.TextField(default='', verbose_name='作者')),
                ('catalog', models.TextField(default='', verbose_name='目录')),
                ('description', models.TextField(default='', verbose_name='描述')),
                ('isbn', models.CharField(default='', max_length=17, verbose_name='ISBN')),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='新书价格')),
                ('image_url', models.ImageField(upload_to='book_cover', verbose_name='封面图片')),
            ],
            options={
                'verbose_name': '书籍',
                'db_table': 'Book',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LogisticsOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='总金额')),
                ('content', models.TextField(default='', verbose_name='运送内容')),
                ('logistics_token', models.CharField(default=b'9sy9GNeHEeex06zgEJ3fJg==', editable=False, max_length=24, verbose_name='物流token')),
                ('logistics_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logistics_agent', to='OnlineBookStore.Account', verbose_name='物流代理商')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='OnlineBookStore.Account', verbose_name='出售者')),
            ],
            options={
                'verbose_name': '运送请求单',
                'db_table': 'LogisticsOrder',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('content', models.TextField(default='', verbose_name='消息内容')),
                ('is_sent', models.BooleanField(default=False, editable=False, verbose_name='是否已经推送')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.Account', verbose_name='用户')),
            ],
            options={
                'verbose_name': '消息',
                'db_table': 'Message',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PaymentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='金额')),
                ('creating_time', models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间')),
                ('deadline', models.DateTimeField(default=1512236461.9028978, verbose_name='支付期限')),
                ('payment_token', models.UUIDField(default=b'9sk59NeHEee/eKzgEJ3fJg==', editable=False, verbose_name='支付token')),
                ('type', models.IntegerField(choices=[(0, '充值'), (1, '购物')], default=0, verbose_name='订单类型')),
                ('content', models.TextField(default='', verbose_name='支付内容')),
                ('is_finished', models.BooleanField(default=False, verbose_name='是否已经完成支付')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.Account', verbose_name='用户')),
            ],
            options={
                'verbose_name': '支付订单',
                'db_table': 'PaymentOrder',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ShoppingOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='总金额')),
                ('content', models.TextField(default='', verbose_name='购物内容')),
                ('shipping_option', models.IntegerField(choices=[(0, '快递'), (1, '优先'), (2, '普通')], default=0, verbose_name='运送选项')),
                ('status', models.IntegerField(choices=[(0, '待支付'), (1, '已支付'), (2, '已发货'), (3, '未发货')], default=0, verbose_name='状态')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.Account', verbose_name='用户')),
                ('payment_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.PaymentOrder', verbose_name='支付订单')),
            ],
            options={
                'verbose_name': '购物订单',
                'db_table': 'ShoppingOrder',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UnactivatedAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('mail', models.EmailField(default='', max_length=254, unique=True, verbose_name='邮箱地址')),
                ('password', models.CharField(default='', max_length=36, verbose_name='密码')),
                ('address', models.CharField(default='', max_length=255, verbose_name='家庭住址')),
                ('activation_token', models.CharField(default=b'9sgBSteHEeeuOazgEJ3fJg==', editable=False, max_length=24, verbose_name='邮箱验证token')),
                ('activation_deadline', models.DateTimeField(default='', verbose_name='邮箱激活期限')),
                ('is_activation_finished', models.BooleanField(default=False, editable=False, verbose_name='是否已经完成激活')),
            ],
            options={
                'verbose_name': '待激活账号',
                'db_table': 'UnactivatedAccount',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid1, editable=False, unique=True, verbose_name='uuid')),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='售价')),
                ('server_fee', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='售价'))], verbose_name='服务费')),
                ('description', models.TextField(default='', verbose_name='描述')),
                ('status', models.IntegerField(choices=[(0, '待售'), (1, '正在售出'), (2, '已售出')], default=0, verbose_name='状态')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.Book', verbose_name='书籍')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.Account', verbose_name='出售者')),
                ('shopping_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.ShoppingOrder', verbose_name='购物订单')),
            ],
            options={
                'verbose_name': '二手书',
                'db_table': 'UsedBook',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='logisticsorder',
            name='shopping_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineBookStore.ShoppingOrder', verbose_name='购物订单'),
        ),
    ]