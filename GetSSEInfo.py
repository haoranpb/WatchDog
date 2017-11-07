# -*- coding:utf-8 -*-
"""
Description: get the first 7 lines information from 'http://sse.tongji.edu.cn/data/list/bkstz'
"""

from selenium import webdriver
import time
import signal


class GetSSEInfo:
    def __init__(self):
        self.url = 'http://sse.tongji.edu.cn/data/list/bkstz'

    def get_sse_info(self):
        print "begin sse"
        driver = webdriver.PhantomJS()
        try:
            driver.get(self.url)
        except:
            message = 'get sse website error\n'
            return message
        time.sleep(0.5)
        i = 1
        message = 'sse information:\n'
        while 1:
            xpath = '/html/body/div[3]/div/div[3]/div/ul/li[' + str(i) + ']/a'
            text = driver.find_element_by_xpath(xpath).text
            if i > 7:
                message = message + '\n'
                break
            message = message + text + '\n'
            i = i + 1

        driver.service.process.send_signal(signal.SIGTERM)
        driver.quit()
        print "quit sse"
        return message


