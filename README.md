# A Python Spider To Get Info From 4m3
[中文文档](http://ludanxer.top/2017/11/25/WatchDog/)
## WHAT'S NEW：
1. I rewrite this program to python3, because more and more famous progams declared to abandon python2
2. Use `lxml` (and `requsets`) to crawl the websites that do not need to login to faster the program
3. Add two new websites：[书伴](https://bookfere.com/) and [电影天堂](http://www.dy2018.com/)

## OVERVIEW:
Use `python3` `selenium` `phantomjs` `lxml` and `requests` to get information from [4m3](4m3.tongji.edu.cn), [SSE](http://sse.tongji.edu.cn/data/list/bkstz), [书伴](https://bookfere.com/), [电影天堂](http://www.dy2018.com/), and send it to your e-mail automatically.**If you are going to run this program, make sure you finish reading this doc. It's not long but useful**
## ATTENTION:
* **You are not allowed to use this program to visit a website too frequently**
*  You can't run the program before you **fill in some of your information**
* You need to **install selenium, phantomjs, lxml, requests** if you haven't
* If you are not going to crawl [4m3](4m3.tongji.edu.cn), [SSE](http://sse.tongji.edu.cn/data/list/bkstz), you can ignore the tip below
* **This program may not work if you are not using `TongJi university`'s WIFI, You need to download TongJi's [VPN](htttps://vpn.tongji.cn)**


## BEFORE RUNNING:
1. In file **`Get4m3Info.py`**: You need to **fill in your student card ID and username**
2. In file **`MailSender.py`**: You need to **fill in your email address, password and reciever's address**, you also need to replace`163` in `smtp.163.com` to your email domain name
3. Install [selenium](http://www.seleniumhq.org/): Use `pip3 install selenium` in the command line to install selenium.
4. Install [lxml](http://lxml.de/) and [requsets](http://docs.python-requests.org/en/master/) in the same way above
5. Install `phantomjs`(on macOS): You can download [phantomjs here](http://phantomjs.org/), and make a copy of `/phantomjs/bin/phantomjs` to `/usr/local/bin/`

## DEPLOY：
This program can be deployed to VPS to send you informaiton at a certain time everyday.

1. Move this program to your VPS, run the order in the command line:  
`scp /path/to/your/spider.zip  root@your ip address:/path/to/your/file`.
2. Install selenium, phantomjs, lxml and requsets on your VPS.
3. Use [Crontab](http://www.adminschoice.com/crontab-quick-reference) to make it run at a certain time. Use `crontab -e` to edit. Add a line      like `0 7 * * * python3 /path/to/your/GetInfo.py` to make it run at 7 everyday in the morning.


## WHAT'S MORE:
If you get any problems while running this program, you can create an issue or send me an [e-mail](mailto:Alseepludan@163.com) to contact me.I'm still working to make this program perfect, if you get any good idea, don't hesitate to contact me!