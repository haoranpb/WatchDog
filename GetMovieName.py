# -*- coding:utf-8 -*-
"""
URL: http://www.dy2018.com/
Description: Get first 5 movie names from the URL above
"""
from lxml import html


class GetMovieName:
    def __init__(self):
        self.url = 'http://www.dy2018.com/'

    def get_movie_name(self):
        print("movie begin")
        response = html.parse(self.url)
        message = 'Movie Name:\n'
        for i in range(1, 6):
            xpath = '/html/body/div/div/div[3]/div[4]/div[1]/div[2]/ul/li[' + str(i) + ']/a/text()'
            content = response.xpath(xpath)
            message = message + str(content)[2:-2] + '\n'
        message += '\n'
        print("movie end")
        return message

