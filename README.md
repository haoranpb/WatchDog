# A Python Spider To Get Info From 4m3

## OVERVIEW:
Use `python3` to get information from [4m3](4m3.tongji.edu.cn), [SSE](http://sse.tongji.edu.cn/data/list/bkstz), [书伴](https://bookfere.com/), and send it to your e-mail automatically.
## ATTENTION:
*  You can't run the program before you **fill in some of your information**
* If you are not going to crawl [4m3](4m3.tongji.edu.cn), [SSE](http://sse.tongji.edu.cn/data/list/bkstz), you can ignore the tip below
* **This program may not work if you are not using `TongJi university`'s WIFI, You need to download TongJi's [VPN](htttps://vpn.tongji.cn)**
  

## Fill In Information:
1. In file **`Get4m3Info.py`**: You need to **fill in your student card ID and username**
2. In file **`MailSender.py`**: You need to **fill in your email address, password and reciever's address**, you also need to replace`163` in `smtp.163.com` to your email domain name

## Dependence:
* requests
* lxml
* selenium
* phantomjs