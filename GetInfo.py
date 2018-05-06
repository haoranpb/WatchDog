#!/usr/bin/python3
"""
Author: 孙浩然
Last modified: 2018/5/6
Description: Use python3 to get information from 4m3 and SSE and send it as E-mail
"""
from get_4m3_info import Get4m3Info
from get_sse_info import GetSSEInfo
from mail_sender import MailSender

if __name__ == '__main__':
    message = ''
    message += Get4m3Info().get_4m3_info()
    message += GetSSEInfo().get_sse_info()
    receivers = [''] # add your own receivers E-mail address, multiple address available
    MailSender().send_mail(message=message, receiver= receivers)
