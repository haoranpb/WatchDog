#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: 孙浩然
Date: 2017.11.25
Description: Use python3 to get information from several website and send it as E-mail
"""
from Get4m3Info import Get4m3Info
from GetSSEInfo import GetSSEInfo
from GetBookNames import GetBookName
from GetMovieName import GetMovieName
from MailSender import MailSender


message = ''
message += Get4m3Info().get_4m3_info()
message += GetSSEInfo().get_sse_info()
# message += GetBookName().get_book_name()
# message += GetMovieName().get_movie_name()
MailSender().send_mail(message=message)
