# -*- coding:utf-8 -*-
"""
URL: http://4m3.tongji.edu.cn/
Description: Get information from 4m3.tongji.edu.cn, only get lines with 'new' in them
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import signal
import socket


class Get4m3Info:
    def __init__(self):
        self.url = "http://4m3.tongji.edu.cn/"
        self.username = 'xxx'  # please fill in your username
        self.passward = 'xxx'  # please fill in your password

    def get_4m3_info(self):
        print("4m3 begin")
        socket.setdefaulttimeout(5)
        driver = webdriver.PhantomJS()
        try:
            driver.get(self.url)
        except socket.timeout:
            message = 'get 4m3 website time out\n'
            return message
        except Exception:  # need to improve
            message = 'get 4m3 website error\n'
            return message
        else:
            elem = driver.find_element_by_xpath('//*[@id="login_box"]/div[2]/div/h2/a')  # 选取“统一身份认证”按钮
            elem.send_keys(Keys.ENTER)  # 登入
            time.sleep(0.5)

            # login
            elem_user = driver.find_element_by_name("Ecom_User_ID")
            elem_user.send_keys(self.username)
            elem_pwd = driver.find_element_by_name("Ecom_Password")
            elem_pwd.send_keys(self.passward)
            elem_login = driver.find_element_by_name("submit")
            elem_login.send_keys(Keys.ENTER)
            time.sleep(0.5)

        # get the message
        i = 2
        message = '4m3:\n'
        while 1:
            xpath = '/html/body/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[' + str(i) + ']'
            line = driver.find_element_by_xpath(xpath).text
            if 'new' not in line:
                message = message + '\n'
                break
            text = line[0:line.rfind('new') - 1]
            message = message + text + '\n'
            i = i + 1

        driver.service.process.send_signal(signal.SIGTERM)
        driver.quit()
        print("4m3 end")
        message += '\n\n'
        return message
