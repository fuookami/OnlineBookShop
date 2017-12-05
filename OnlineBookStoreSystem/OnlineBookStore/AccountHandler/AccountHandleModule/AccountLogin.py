from ...Models import Account, UnactivatedAccount


def login(mail, password):
    ret = Account.login(mail, password)

    if ret["code"] == 1 and UnactivatedAccount.has_waiting_activated_account_mail_is(mail):
        ret["code"] = 3

    return ret
