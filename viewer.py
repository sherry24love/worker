# coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import os
from time import sleep

chorme_options = webdriver.ChromeOptions()

while True:
    print("current directory is {}".format(os.getcwd()))
    # os.system(command)
    # 60.17.252.34:4225
    # 115.213.189.105
    ip = '182.38.102.13:4258'
    ip = '114.99.3.81:4267'
    ip = '117.69.241.82:4209'
    url = 'http://nesw.xijspex.cn/LJOyH/xqnwthemjlplsiGjvjb.shtml'
    url = "http://god.klafer.cn/lC/dvtqfgzlaaysiGfyjd.html"
    url = "http://www.baidu.com"
    url = [
        "http://www.baidu.com",
        "http://www.qq.com"
    ]
    proxy = 'socks5://{}'.format(ip)

    # chorme_options.add_argument("--proxy-server={}".format(proxy))
    ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 MicroMessenger/6.5.8 NetType/WIFI Language/zh_CNMozilla"
    ua = "Mozilla/5.0 (Linux; Android 9; MI 8 Lite Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044904 Mobile Safari/537.36 MMWEBID/6714 MicroMessenger/7.0.7.1521(0x27000739) Process/tools NetType/WIFI Language/zh_CN"
    chorme_options.add_argument("user-agent={}".format(ua))
    brower = webdriver.Chrome(options=chorme_options)
    # open first tab
    brower.get(url[0])
    brower.implicitly_wait(10)
    # open second tab

    brower.execute_script("window.open('','_blank');")
    brower.switch_to.window(brower.window_handles[-1])
    brower.get( url[1] )

    print(brower.get_cookies())
    brower.implicitly_wait(10)

    try:
        pre = brower.find_element_by_xpath("/html/body")
        if pre:
            print(pre.text)
    except NoSuchElementException:
        pass
    sleep(5)
    break
    # brower.close()
