from ...Models import Account, Message


def generate_message(_uuid, _title, _content):
    new_obj = Message(
        account=Account.objects.filter(uuid=_uuid).get(),
        title=_title,
        content=_content
    )
    new_obj.save()
