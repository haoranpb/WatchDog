"""
Author: 孙浩然
Last modified: 2018/4/28
Description: Send an E-mail by python
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class MailSender:

    def __init__(self):
        self.sender = 'xxx@xxx.com'  # Fill in sender
        self.username = 'xxx@xxx.com'  # Fill in your E-mail username
        self.password = 'xxx'  # Fill in your E-mail password

                        # Fill in default receiver and other information below
    def send_mail(self, message='Information', receiver='xxx@xxx.com', subject='每日校园资讯'):
        print("E-mail Begin")
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.sender
        msg['To'] = ','.join(receiver)

        smtp = smtplib.SMTP_SSL('smtp.163.com', 465, timeout=120)  # Replace 163 to your E-mail domain
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, receiver, msg.as_string())
        smtp.quit()
        print("E-mail End")
