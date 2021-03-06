# coding: utf8

import os

from email.mime.text import MIMEText
import smtplib

# email config
MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.163.com"
MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = ['hebee0954@gmail.com', "609926981@qq.com"]


def send_mail(filename):
    """ send mail """
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()

        message = MIMEText(content, 'plain', 'utf8')
        message['From'] = MAIL_USERNAME
        message['To'] = ADMINS[1]
        message['Subject'] = filename

        try:
            print(MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD)
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(MAIL_SERVER, MAIL_PORT)
            smtp_obj.login(MAIL_USERNAME, MAIL_PASSWORD)
            smtp_obj.sendmail(MAIL_USERNAME, ADMINS, message.as_string())
            print("send mail success")
        except smtplib.SMTPDataError as e:
            print('faild', e)
