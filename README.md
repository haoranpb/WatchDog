# A Simple Python Spider
## Overview:
use python to get information from 4m3 and sse, and send them to your e-mail automatically
## Attention:
* you can't run the program before you **fill in some of your information**
* you may need to **download some libraries and web driver** yourself

## Before running:
1. Library used in this program:`selenium`, `smtplib`, `time`, `email`,you can download them in command line like: `pip install selenium`
2. I suppose you use chrome as your browser, you need to download chrome diver, you can get [reference here](http://blog.csdn.net/cz9025/article/details/70160273). Of course you can use other browsers, but you also need to download the corresponding driver.
3. If you use other browsers, remember to change `webdriver.Chrome()` into `webdriver.browser()`. `webdriver.Chrome()` is in both `Get4m3Info.py` and `GetSSEInfo.py`.
4. You need to **fill in your student card ID and username** in `Get4m3Info.py`
5. You need to **fill in your email address, password and reciever's address**, you also need to change `smtp.163.com` to your email

