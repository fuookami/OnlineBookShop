import uuid

from django.db import models
from django.core.validators import MinValueValidator

from ..Models import Account, ShoppingOrder
from PublicModule import IdentifierGenerator


class LogisticsOrder(models.Model):
    uuid = models.UUIDField(
        auto_created=True,
        default=uuid.uuid1,
        unique=True,
        editable=False,
        verbose_name='uuid'
    )
    logistics_agent = models.ForeignKey(
        Account,
        related_name='logistics_agent',
        verbose_name="物流代理商"
    )
    amount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ],
        verbose_name="总金额"
    )
    shopping_order = models.ForeignKey(
        ShoppingOrder,
        verbose_name="购物订单"
    )
    seller = models.ForeignKey(
        Account,
        null=True,
        related_name='seller',
        verbose_name="出售者"
    )
    content = models.TextField(
        default='',
        verbose_name="运送内容"
    )
    logistics_token = models.CharField(
        max_length=24,
        default=IdentifierGenerator.base64_uuid_generator(),
        editable=False,
        verbose_name='物流token'
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "LogisticsOrder"
        managed = True
        verbose_name = "运送请求单"
