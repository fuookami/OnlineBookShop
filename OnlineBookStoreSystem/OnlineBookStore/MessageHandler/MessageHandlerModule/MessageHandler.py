import base64

from ...Models import Message
from PublicModule.HTTPResponseDispose import before_send_dispose


def get_message_count(uuid):
    return before_send_dispose(Message.get_message_count_by_account_uuid(uuid))


def get_messages(uuid, bg_index, ed_index):
    return before_send_dispose(Message.get_messages_by_account_uuid(uuid, bg_index, ed_index))
