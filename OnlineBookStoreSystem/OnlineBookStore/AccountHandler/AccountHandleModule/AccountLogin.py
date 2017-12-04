from ...Models import Account


def login(mail, password):
    return Account.login(mail, password)
