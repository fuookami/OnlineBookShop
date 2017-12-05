import base64
import datetime

from .MailActivationGenerator import generate_mail_activation
from ...Models import UnactivatedAccount, Account


def registered_account(_mail, _password, _address, _name):
    ret = {}

    new_obj = UnactivatedAccount(
        mail=_mail,
        password=_password,
        address=_address,
        name=_name,
        activation_deadline=datetime.datetime.now() + datetime.timedelta(days=1)
    )

    if Account.has_account_mail_is(_mail) or UnactivatedAccount.has_waiting_activated_account_mail_is(new_obj.mail):
        ret["code"] = 1
    elif generate_mail_activation(
            new_obj.name, new_obj.mail, new_obj.activation_deadline.strftime("%Y-%m-%d %H:%M:%S"),
            new_obj.activation_token):
        new_obj.save()
        ret["code"] = 0
        ret["deadline"] = new_obj.activation_deadline.strftime("%Y-%m-%d %H:%M:%S")
    else:
        ret["code"] = 2

    return ret


def activate_account(token):
    obj = UnactivatedAccount.get_waiting_activated_account_by_token(token)

    if obj is not None:
        obj.is_activation_finished = True
        obj.save()

        new_obj = Account(
            mail=obj.mail,
            password=obj.password,
            name=obj.name,
            address=obj.address,
        )
        new_obj.save()
        return True
    else:
        return False
