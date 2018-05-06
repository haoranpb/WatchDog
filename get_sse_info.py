"""
Author: 孙浩然
Last modified: 2018/5/6
Description: Get the first 6 lines information from 同济大学软件学院 -> 学院通知
"""

from lxml import html
import time

class GetSSEInfo:
    def __init__(self):
        self.url = 'http://sse.tongji.edu.cn/data/list/xwdt'

    def get_sse_info(self):
        print("SSE Begin")
        try:
            response = html.parse(self.url)
        except Exception: # need to improve, maybe send error message ?
            message = 'Get SSE Info Error\n\n'
            return message
        else:
            time.sleep(0.5)
            message = 'SSE Info:\n\n'
            content = response.xpath('/html/body/div[3]/div/div[3]/div/ul/li/a/text()')[0:7]
            for info in content:
                message = message + str(info)[22:-22] + '\n'
            message += '\n\n\n'
            print("SSE End")
            return message