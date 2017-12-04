import base64

from django.shortcuts import render

from .AccountRegisterModule import registered_account, activate_account
from .AccountHandleModule import login
from PublicModule.HTTPResponseDispose import before_send_dispose


def registered_account_request(request):
    data = request.POST
    return before_send_dispose(registered_account(
        bytes.decode(base64.b64decode(data["mail"])),
        bytes.decode(base64.b64decode(data["password"])),
        bytes.decode(base64.b64decode(data["address"])),
        bytes.decode(base64.b64decode(data["name"]))
    ))


def activate_account_request(request, token):
    if activate_account(token):
        return render(request, '../WebRoot/activation_ok.html')
    else:
        return render(request, '../WebRoot/activation_fail.html')


def login_request(request):
    data = request.POST
    return before_send_dispose(login(
        bytes.decode(base64.b64decode(data["mail"])),
        bytes.decode(base64.b64decode(data["password"]))
    ))
