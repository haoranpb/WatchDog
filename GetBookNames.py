# -*- coding: utf-8 -*-
"""
URL: https://bookfere.com/
Description: Get first 5 book names from the URL above
The reason of using request: Can't open 'https' by html.parse
"""
from lxml import html
import requests
import socket


class GetBookName:
    def __init__(self):
        self.url = 'https://bookfere.com/'

    def get_book_name(self):
        print("book begin")
        socket.setdefaulttimeout(5)
        try:
            page = requests.get(self.url)
        except socket.timeout:
            message = 'Get book name time out\n'
            return message
        except Exception:
            message = 'Get book name error\n'
            return message
        else:
            response = html.fromstring(page.text)
            message = 'Book Name:\n'
            for i in range(1, 6):
                xpath = '//div[@class="recomm-2"]/ul/li[' + str(i) + ']/a/text()'
                content = response.xpath(xpath)
                message = message + str(content)[2:-2] + '\n'
            message += '\n\n\n'
            print("book end")
            return message
