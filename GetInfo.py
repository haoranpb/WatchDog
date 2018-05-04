#!/usr/bin python3
"""
Author: 孙浩然
Last modified: 2018/5/4
Description: Use python3 to get information from 4m3 and SSE and send it as E-mail
"""
from Get4m3Info import get4m3Info
from GetSSEInfo import getSSEInfo
from MailSender import MailSender

message = ''
message += get4m3Info().get_4m3_info()
message += getSSEInfo().get_sse_info()
receivers = [''] # add your own receivers E-mail address, multiple address available
MailSender().send_mail(message=message,receiver= receivers)
