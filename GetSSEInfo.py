# -*- coding:utf-8 -*-
"""
本程序抓取软件学院 学院网/信息中心/学院通知 的前6条通知
url:   http://sse.tongji.edu.cn/Data/List/xwdt
"""

from selenium import webdriver
import time


class GetSSEInfo:
    def __init__(self):
        self.url = 'http://sse.tongji.edu.cn/data/list/bkstz'

    def get_sse_info(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(0.3)
        i = 1
        message = 'sse information:\n'
        while(1):
            xpath = '/html/body/div[3]/div/div[3]/div/ul/li[' + str(i) + ']/a'
            text = driver.find_element_by_xpath(xpath).text
            if i > 7:
                message = message + '\n'
                break
            message = message + text + '\n'
            i = i + 1

        driver.close()
        driver.quit()
        return message


