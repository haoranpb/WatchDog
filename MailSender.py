# coding: utf-8
"""
date:2017.10.20
Description of this program:
send an E-mail(including a string) by python
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender:
    def __init__(self):
        self.sender = 'xxx@xxx.com'    # 请输入发件人邮箱
        self.username = 'xxx@xxx.com'  # 请输入发送邮件的邮箱地址
        self.password = 'xxx'          # 请输入邮箱密码

    def send_mail(self, message='Hello World!', receiver='xxx@xxx.com',  # 请输入默认收件人邮箱地址
                  subject='this is an auto sending email'):     # 请输入默认的邮件主题
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.sender
        msg['To'] = receiver

        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')    # 请记得修改为您使用的邮箱
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, receiver, msg.as_string())
        smtp.quit()

