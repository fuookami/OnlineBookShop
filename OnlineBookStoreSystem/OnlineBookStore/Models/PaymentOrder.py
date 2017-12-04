import uuid
import time

from django.db import models
from django.core.validators import MinValueValidator

from ..Models import Account
from PublicModule import IdentifierGenerator

PaymentTypeCode = (
    (0, '充值'),
    (1, '购物')
)


class PaymentOrder(models.Model):
    uuid = models.UUIDField(
        auto_created=True,
        default=uuid.uuid1,
        unique=True,
        editable=False,
        verbose_name='uuid'
    )
    account = models.ForeignKey(
        Account,
        verbose_name="用户"
    )
    amount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ],
        verbose_name="金额"
    )
    creating_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="订单创建时间"
    )
    deadline = models.DateTimeField(
        default=time.time(),
        verbose_name="支付期限"
    )
    payment_token = models.UUIDField(
        max_length=24,
        default=IdentifierGenerator.base64_uuid_generator(),
        editable=False,
        verbose_name='支付token'
    )
    type = models.IntegerField(
        default=0,
        choices=PaymentTypeCode,
        verbose_name="订单类型"
    )
    content = models.TextField(
        default='',
        verbose_name="支付内容"
    )
    is_finished = models.BooleanField(
        default=False,
        verbose_name="是否已经完成支付"
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "PaymentOrder"
        managed = True
        verbose_name = "支付订单"
