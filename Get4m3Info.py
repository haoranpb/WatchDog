"""
Author: 孙浩然
Last modified: 2018/5/4
Description: Use selenium + chromedriver(headless) to crawl 4m3
Issue: 
    1. Have trouble using requests + lxml to crawl 4m3
    2. Enable '--no-sandbox' option for deploying on ECS
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class get4m3Info:
    def __init__(self):
        self.url = 'http://4m3.tongji.edu.cn/' # automatically redirect to login page
        self.username = 'xxx'  # please fill in your username
        self.passward = 'xxx'  # please fill in your password

    def get_4m3_info(self):
        print("4m3 Begin")
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
        options.add_argument('--lang=en-US,en')
        # options.add_argument('--no-sandbox') # uncomment to work on Linux
        driver = webdriver.Chrome(chrome_options= options)

        try:
            driver.get(self.url)
            driver.implicitly_wait(5) # much better and quicker than time.sleep()
            # login
            elem_user = driver.find_element_by_name("Ecom_User_ID")
            elem_user.send_keys(self.username)
            elem_pwd = driver.find_element_by_name("Ecom_Password")
            elem_pwd.send_keys(self.passward)
            elem_login = driver.find_element_by_name("submit")
            elem_login.send_keys(Keys.ENTER)
        except Exception: # need to improve, maybe send error message ?
            message = 'Get 4m3 Info Error\n\n'
            driver.quit()
            return message
        else:
            driver.implicitly_wait(5)
            # get the message
            message = '4m3 Info:\n\n'
            lines = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[3]/div/div/div/table/tbody').text.split('\n')
            for line in lines:
                if 'new' in line:
                    message = message + line + '\n'
            message += '\n\n'
            driver.quit()
            print("4m3 End")
            return message