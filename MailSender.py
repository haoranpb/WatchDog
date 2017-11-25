# -*- coding:utf-8 -*-
"""
Description: Send an E-mail by python
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender:
    def __init__(self):
        self.sender = 'xxx@xxx.com'
        self.username = 'xxx@xxx.com'  # fill in your username
        self.password = 'xxx'  # fill in your password

    def send_mail(self, message='Hello World!', receiver='xxx@xxx.com', subject='This is an auto sending email'):
        print("email begin")
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.sender
        msg['To'] = receiver

        smtp = smtplib.SMTP_SSL('smtp.163.com', 465, timeout=120)  # replace 163 to your domain name
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, receiver, msg.as_string())
        smtp.quit()
        print("email end")

