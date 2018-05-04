# A Python Spider To Get Info From 4m3

## OVERVIEW:
Use python3 to get information from [4m3.tongji.edu.cn](4m3.tongji.edu.cn), [sse.tongji.edu.cn](http://sse.tongji.edu.cn/data/list/bkstz) and send it to your E-mail automatically.
## ATTENTION:
*  You can't run the program before you **fill in some of your information**
*  **This program may not work if you are not using `TongJi university`'s WIFI, You may need to download TongJi's [VPN](htttps://vpn.tongji.cn)**


## Fill In Information:
1. In file `Get4m3Info.py`: You need to **fill in your student card username and password**
2. In file `MailSender.py`: You need to **fill in sender, your email address, password, you also need to replace`163` in `smtp.163.com` to your email domain name**
3. In file `GetInfo.py` : You need to **fill in receivers E-mail address**

## Dependence:
* lxml
* selenium
* google-chrome
* chromedriver