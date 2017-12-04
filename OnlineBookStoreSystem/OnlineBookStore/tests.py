import base64
import json

from django.test import TestCase
from django.conf import settings, global_settings

from PublicModule.HTTPResponseDispose import before_send_dispose

from .AccountHandler.AccountRegisterModule.AccountRegister import registered_account


# Create your tests here.
def test_pattern(request, token1 = "abc", token2 = "bcd"):
    print(token1, token2)
    return before_send_dispose({})


def test_server_ip(request):
    print(settings.BASE_DIR),
    print(settings.ALLOWED_HOSTS)
    return before_send_dispose({})


def test_register(request):
    data = {
        "mail": bytes.decode(base64.b64encode(str.encode("373611500@qq.com"))),
        "password": bytes.decode(base64.b64encode(str.encode("373611500"))),
        "name": bytes.decode(base64.b64encode(str.encode("李伟文"))),
        "address": bytes.decode(base64.b64encode(str.encode("江苏省南京市江宁区胜太西路169号")))
    }
    return registered_account(data)
