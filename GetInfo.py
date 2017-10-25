#!/usr/bin/env python
# coding:utf-8

from GetSSEInfo import GetSSEInfo
from Get4m3Info import Get4m3Info
import MailSender


sse = GetSSEInfo()
g4m3 = Get4m3Info()

message = ''
text = sse.get_sse_info()
message = message + text
text = g4m3.get_4m3_info()
message = message + text

mail = MailSender.MailSender()
mail.send_mail(message)  # 您可以在这里直接修改“收件人”和“邮箱主题” send_mail(message, reciever, subjecet)
