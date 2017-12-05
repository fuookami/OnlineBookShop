import base64
import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..Models import Book, Account, ShoppingOrder

UsedBookStatusCode = (
    (0, '待售'),
    (1, '正在售出'),
    (2, '已售出')
)


class UsedBook(models.Model):
    uuid = models.UUIDField(
        auto_created=True,
        default=uuid.uuid1,
        unique=True,
        editable=False,
        verbose_name='uuid'
    )
    book = models.ForeignKey(
        Book,
        verbose_name="书籍"
    )
    seller = models.ForeignKey(
        Account,
        verbose_name="出售者"
    )
    price = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ],
        verbose_name="售价"
    )
    server_fee = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ],
        verbose_name="服务费"
    )
    shopping_order = models.ForeignKey(
        ShoppingOrder,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="购物订单"
    )
    description = models.TextField(
        default='',
        verbose_name="描述"
    )
    status = models.IntegerField(
        default=0,
        choices=UsedBookStatusCode,
        verbose_name="状态"
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "UsedBook"
        managed = True
        verbose_name = "二手书"

    @staticmethod
    def get_server_fee(price):
        return price * 0.05

    @staticmethod
    def get_on_selling_used_book_of_book(_uuid):
        book_obj = Book.get_by_uuid(_uuid)
        objs = UsedBook.objects.filter(book=book_obj).filter(status=0).order_by("price").all()

        ret = []
        for obj in objs:
            ret.append({
                "uuid": bytes.decode(base64.b64encode(obj.uuid.bytes)),
                "seller_name": obj.seller.name,
                "seller_mail": obj.seller.mail,
                "price": obj.price,
                "description": obj.description
            })
        return ret
