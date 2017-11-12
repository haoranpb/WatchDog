# A Python Spider To Get Info From 4m3.tongji.edu.cn
## OVERVIEW:
Use python+selenium+phantomjs to get information from [4m3](4m3.tongji.edu.cn) and [sse](http://sse.tongji.edu.cn/data/list/bkstz), and send it to your e-mail automatically.
## WARNING:
* **You are not allowed to use this program to visit a website too frequently.**
* **This program may not work if you are not using `TongJi university`'s WIFI, You need to download TongJi's [VPN](htttps://vpn.tongji.cn)**


## ATTENTION:
* You can't run the program before you **fill in some of your information**
* You need to **download selenium and phantomjs** yourself

## BEFORE RUNNING:
1. In file **`Get4m3Info.py`**: You need to **fill in your student card ID and username**
2. In file **`MailSender.py`**: You need to **fill in your email address, password and reciever's address**, you also need to replace`163` in `smtp.163.com` to your email domain name
3. Install [selenium](http://www.seleniumhq.org/): Use `pip install selenium` in the command line to install selenium.
4. Install phantomjs(on macOS): You can download [phantomjs here](http://phantomjs.org/), and make a copy of `/phantomjs/bin/phantomjs` to `/usr/local/bin/`.

## DEPLOY
This program can be deployed to VPS to send you informaiton at a certain time everyday.

1. Move this program to your VPS, run the order in the command line:  
`scp /path/to/your/Spider.zip  root@your ip address:/path/to/your/file`.
2. Install selenium and phantomjs on your VPS.
3. Use [Crontab](http://www.adminschoice.com/crontab-quick-reference) to make it run at a certain time. Use `crontab -e` to edit. Add a line      like `0 7 * * * python /path/to/your/GetInfo.py` to make it run at 7 everyday in the morning.


## CONTACT:
If you get any problems when running this program, you can create an issue or send me an [e-mail](mailto:Alseepludan@163.com) to contact me.