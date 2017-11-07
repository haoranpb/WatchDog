#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Data：2017.11.7
Author: 孙浩然
Description: Get 4m3.tongji.edu.cn automatically and send it to your e-mail
"""

import GetSSEInfo
import Get4m3Info
import MailSender


sse = GetSSEInfo.GetSSEInfo()
g4m3 = Get4m3Info.Get4m3Info()

message = ''
text = g4m3.get_4m3_info()
message = message + text
# text = sse.get_sse_info() # if you want to get sse information as well
# message = message + text  # remove both '#' in front of the line

mail = MailSender.MailSender()
mail.send_mail(message)

