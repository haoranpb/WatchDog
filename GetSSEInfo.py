# -*- coding:utf-8 -*-
"""
URL: http://sse.tongji.edu.cn/data/list/bkstz
Description: get the first 6 lines information from URL above
"""
from lxml import html


class GetSSEInfo:
    def __init__(self):
        self.url = 'http://sse.tongji.edu.cn/data/list/bkstz'

    def get_sse_info(self):
        print("SSE begin")
        response = html.parse(self.url)
        message = 'SSE Info:\n'
        for i in range(1, 7):
            xpath = '/html/body/div[3]/div/div[3]/div/ul/li[' + str(i) + ']/a/text()'
            content = response.xpath(xpath)
            message = message + str(content)[26:-22] + '\n'
        message += '\n\n\n'
        print("SSE end")
        return message

