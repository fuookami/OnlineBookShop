import smtplib
from email.header import Header
from email.mime.text import MIMEText

from django.conf import settings

register_activation_emil_subject = "在线书店账号激活邮件"
register_activation_sender_mail = "fuookami@163.com"
register_activation_sender_password = "a84228a"
register_activation_sender = "在线书店 <%s>" % register_activation_sender_mail
register_activation_sender_sever = "smtp.163.com"
register_activation_emil_content = \
    '''
        <p>%s你好，这是在线书店的激活邮件。</p>
        <p>请在进入以下链接，在%s前完成激活：</p>
        <p><a href="%s">点击进行激活</a></p>
    '''
register_activation_host = "http://127.0.0.1:8000/account/register/activation_token=" \
    if settings.DEBUG else ""


def generate_mail_activation(name, target_mail, deadline, token):
    content = (register_activation_emil_content % (name, deadline, register_activation_host + token))

    mail = MIMEText(content, "html")
    mail["From"] = Header(register_activation_sender)
    mail["To"] = Header(target_mail)
    mail["Subject"] = Header(register_activation_emil_subject)

    try:
        server = smtplib.SMTP()
        server.connect(register_activation_sender_sever)
        server.login(register_activation_sender_mail, register_activation_sender_password)
        server.sendmail(register_activation_sender, target_mail, mail.as_string())

        server.quit()
        return True
    except Exception as e:
        print(e.args, e.__doc__)
        return False
