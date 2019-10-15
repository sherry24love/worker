# coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import os
from time import sleep
from utils.vpn import vpn
from utils.ua import ua as user_agent
import random

while True:
    print("current directory is {}".format(os.getcwd()))
    # os.system(command)
    # 60.17.252.34:4225
    # 115.213.189.105
    ip = '58.218.200.248:6507'
    v = vpn()
    #ip = v.getIp()
    url = [
        "http://www.roclj.cn/bexzlkdmxnaxdrigGxPBRD.htm#1571061975673",
        "http://god.klafer.cn/lC/dvtqfgzlaaysiGfyjd.html"
    ]
    url = [
        "http://www.baidu.com",
        "http://www.baidu.com"
    ]

    chorme_options = webdriver.ChromeOptions()
    chorme_options.add_argument('disable-infobars')
    chorme_options.add_argument("test-type")
    chorme_options.add_argument("disable-gpu")
    chorme_options.add_experimental_option(
        "excludeSwitches", ["ignore-certificate-errors", "enable-automation"])
    proxy = 'socks5://{}'.format(ip)
    # chorme_options.add_argument("--proxy-server={}".format(proxy))
    """ 获取一条UA """
    user_agent_object = user_agent()
    ua = user_agent_object.get_wechat_ua()

    chorme_options.add_argument("user-agent={}".format(ua))
    brower = webdriver.Chrome(options=chorme_options)
    # open first tab
    brower.get(url[0])
    brower.implicitly_wait(10)
    # open second tab

    brower.execute_script("window.open('','_blank');")
    brower.switch_to.window(brower.window_handles[-1])
    brower.get(url[1])

    brower.implicitly_wait(10)
    sleep(3)

    try:
        js = "document.querySelector('.spread').click();setTimeout(()=>{window.scrollTo(0,10000)},1500)"
        brower.execute_script(js)
    except:
        pass

    sleep(random.randint(10, 40))

    brower.close()
    brower.quit()
    break
