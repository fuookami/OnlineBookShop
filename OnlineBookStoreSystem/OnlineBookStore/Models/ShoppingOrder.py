import uuid

from django.db import models
from django.core.validators import MinValueValidator

from ..Models import Account, PaymentOrder

ShippingOption = (
    (0, '快递'),
    (1, '优先'),
    (2, '普通')
)


ShoppingOrderStatusCode = (
    (0, '待支付'),
    (1, '已支付'),
    (2, '已发货'),
    (3, '未发货')
)


class ShoppingOrder(models.Model):
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
        verbose_name="总金额"
    )
    content = models.TextField(
        default='',
        verbose_name="购物内容"
    )
    shipping_option = models.IntegerField(
        default=0,
        choices=ShippingOption,
        verbose_name="运送选项"
    )
    payment_order = models.ForeignKey(
        PaymentOrder,
        verbose_name="支付订单"
    )
    status = models.IntegerField(
        default=0,
        choices=ShoppingOrderStatusCode,
        verbose_name="状态"
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "ShoppingOrder"
        managed = True
        verbose_name = "购物订单"
