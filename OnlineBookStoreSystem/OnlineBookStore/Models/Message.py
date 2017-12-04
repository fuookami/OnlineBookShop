import uuid

from django.db import models

from ..Models import Account


class Message(models.Model):
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
    title = models.TextField(
        default='',
        verbose_name="消息标题"
    )
    content = models.TextField(
        default='',
        verbose_name="消息内容"
    )
    is_sent = models.BooleanField(
        default=False,
        editable=False,
        verbose_name="是否已经推送"
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "Message"
        managed = True
        verbose_name = "消息"

    @staticmethod
    def get_messages_by_account_uuid(_uuid, bg_index=0, ed_index=-1):
        account_obj = Account.objects.filter(uuid=_uuid)

        ret = {
            "messages": []
        }

        objs = Message.objects.filter(account=account_obj).all()[bg_index: ed_index]
        for obj in objs:
            ret["messages"].append({
                "title": obj.title,
                "content": obj.content,
                "first_sent": not obj.is_sent
            })

        Message.objects.filter(account=account_obj).all().update(is_sent=True)
        return ret

    @staticmethod
    def get_message_count_by_account_uuid(_uuid):
        account_obj = Account.objects.filter(uuid=_uuid)

        ret = {
            "counts": account_obj.count(),
            "new_counts": account_obj.filter(is_sent=False).count()
        }

        return ret
