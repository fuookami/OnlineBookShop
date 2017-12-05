import uuid
import datetime

from django.db import models

from PublicModule import IdentifierGenerator


class UnactivatedAccount(models.Model):
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
    activation_token = models.CharField(
        max_length=24,
        default=IdentifierGenerator.base64_uuid_generator(),
        editable=False,
        verbose_name='邮箱验证token'
    )
    activation_deadline = models.DateTimeField(
        default='',
        verbose_name="邮箱激活期限"
    )
    is_activation_finished = models.BooleanField(
        default=False,
        editable=False,
        verbose_name="是否已经完成激活"
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "UnactivatedAccount"
        managed = True
        verbose_name = "待激活账号"

    @staticmethod
    def get_waiting_activated_account_by_mail(target_mail):
        return UnactivatedAccount.objects.filter(mail=target_mail)\
            .filter(activation_deadline__gt=datetime.datetime.now())\
            .filter(is_activation_finished=False).get()

    @staticmethod
    def has_waiting_activated_account_mail_is(target_mail):
        return UnactivatedAccount.objects.filter(mail=target_mail) \
            .filter(activation_deadline__gt=datetime.datetime.now()) \
            .filter(is_activation_finished=False).exists()

    @staticmethod
    def get_waiting_activated_account_by_token(token):
        return UnactivatedAccount.objects.filter(activation_token=token) \
            .filter(activation_deadline__gt=datetime.datetime.now()) \
            .filter(is_activation_finished=False).get()
