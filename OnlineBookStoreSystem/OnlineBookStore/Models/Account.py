import uuid
import base64

from django.db import models
from django.core.validators import MinValueValidator

AccountTypeCode = (
    (0, '平台管理员'),
    (1, '运送代理商'),
    (2, '普通用户')
)


class Account(models.Model):
    uuid = models.UUIDField(
        auto_created=True,
        default=uuid.uuid1,
        unique=True,
        editable=False,
        verbose_name='uuid'
    )
    mail = models.EmailField(
        default='',
        unique=True,
        verbose_name='邮箱地址'
    )
    password = models.CharField(
        max_length=36,
        default='',
        verbose_name='密码'
    )
    name = models.CharField(
        max_length=24,
        default='',
        verbose_name='姓名'
    )
    address = models.CharField(
        max_length=255,
        default='',
        verbose_name='家庭住址'
    )
    balance = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ],
        verbose_name='余额（分）'
    )
    type = models.IntegerField(
        default=2,
        choices=AccountTypeCode,
        verbose_name='用户类型代码'
    )
    trolley = models.TextField(
        default='',
        editable=False,
        verbose_name='购物车信息'
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "Account"
        managed = True
        verbose_name = "账号"

    @staticmethod
    def has_account_mail_is(_mail):
        return Account.objects.filter(mail=_mail).exists()

    @staticmethod
    def get_account_by_mail(_mail):
        return Account.objects.filter(mail=_mail).get()

    @staticmethod
    def get_account_by_uuid(_uuid):
        return Account.objects.filter(uuid=_uuid).get()

    @staticmethod
    def login(_mail, _password):
        ret = {}
        if not Account.has_account_mail_is(_mail):
            ret["code"] = 1
        else:
            obj = Account.get_account_by_mail(_mail)

            if obj.password == _password:
                ret["code"] = 0
                ret["uuid"] = bytes.decode(base64.b64encode(obj.uuid.bytes))
                ret["type"] = obj.type
                ret["name"] = bytes.decode(base64.b64encode(str.encode(obj.name)))
            else:
                ret["code"] = 2

        return ret
