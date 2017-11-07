# coding: utf-8
"""
Date: 2017.10.20
Author: 孙浩然
Description: send an E-mail(including a string) by python
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender:
    def __init__(self):
        self.sender = 'asleepludan@163.com'
        self.username = 'asleepludan@163.com'  # 发邮件邮箱
        self.password = 'Sy19971o14'

    def send_mail(self, message='Hello World!', receiver='asleepludan@163.com', subject='this is an auto sending email'):
        print "email"
        msg = MIMEText(message, 'plain', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.sender
        msg['To'] = receiver

        smtp = smtplib.SMTP_SSL('smtp.163.com', 465, timeout=120)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, receiver, msg.as_string())
        smtp.quit()
        print "finish"

