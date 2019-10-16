# coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import os
from time import sleep
from utils.vpn import vpn
from utils.ua import ua as user_agent
from utils.links import links
import random

time = 0
debug = True
v = vpn(debug)
user_agent_object = user_agent()
link_object = links(debug)


while True:
    print("current directory is {}".format(os.getcwd()))
    time = time+1
    # os.system(command)
    # 60.17.252.34:4225
    # 115.213.189.105
    ip = '58.218.200.248:6507'
    if debug is False:
        ip = v.getIp()

    """ 获取可以用的APP信息 """

    chorme_options = webdriver.ChromeOptions()
    chorme_options.add_argument('disable-infobars')
    chorme_options.add_argument("test-type")
    chorme_options.add_argument("disable-gpu")
    chorme_options.add_experimental_option(
        "excludeSwitches", ["ignore-certificate-errors", "enable-automation"])

    """ 获取一条UA """
    ua = user_agent_object.get_wechat_ua()
    chorme_options.add_argument("user-agent={}".format(ua))

    if debug is False:
        proxy = 'socks5://{}'.format(ip)
        chorme_options.add_argument("--proxy-server={}".format(proxy))

    # 设置浏览器参数
    brower = webdriver.Chrome(options=chorme_options)

    apps = link_object.get_apps()
    brower.get('http://ip-api.com/json')
    brower.implicitly_wait(3)
    try:
        body = brower.find_element_by_xpath("/html/body/pre")
    except NoSuchElementException:
        print("IP信号不好切下一组IP")
        continue

    # check ip is ok
    for idx in range(len(apps)):
        print(apps[idx])
        # open {idx} tab
        brower.execute_script("window.open('','_blank');")
        brower.switch_to.window(brower.window_handles[-1])
        url = link_object.get_links(0)
        print("正在为您打开链接{}".format(url))
        brower.get(url)
        brower.implicitly_wait(10)
        try:
            print("执行界面的滑动")
            js = "document.querySelector('.spread').click();setTimeout(()=>{window.scrollTo(0,10000)},1500)"
            brower.execute_script(js)
        except:
            pass
        print("在当前页面停留5到20秒")
        sleep(random.randint(5, 30))

    print("补时停留")
    sleep(random.randint(5, 20))

    brower.close()
    print("关闭浏览器")
    brower.quit()
    if debug is True:
        break
    if time > 20:
        break
