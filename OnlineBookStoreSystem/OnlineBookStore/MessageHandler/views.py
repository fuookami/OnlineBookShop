import base64

from .MessageHandlerModule import get_message_count, get_messages
from PublicModule.HTTPResponseDispose import before_send_dispose


def get_message_count_request(request):
    data = request.POST
    return before_send_dispose(get_message_count(base64.b64decode(data["uuid"])))


def get_message_request(request):
    data = request.POST
    return before_send_dispose(get_messages(
        base64.b64decode(data["uuid"]), data["bg_index"], data["ed_index"]))
