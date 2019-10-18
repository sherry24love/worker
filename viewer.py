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
import configparser
import json

time = 0
debug = False

# 获取配置文件
cf = configparser.ConfigParser()
path = os.getcwd()
config_file = os.path.join(path, 'data', 'config.ini')
cf.read(config_file)
conf_sections = cf.sections()
url = cf.get('vpn', 'url')

# 初始化VPN
v = vpn(url, debug)
user_agent_object = user_agent()
link_object = links(debug)


while True:
    print("current directory is {}".format(os.getcwd()))
    time = time+1
    # os.system(command)

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
        ip = v.getIp()
        if ip is False:
            print("本次IP获取失败")
            break
        proxy = 'socks5://{}'.format(ip)
        chorme_options.add_argument("--proxy-server={}".format(proxy))
    exit
    # 设置浏览器参数
    brower = webdriver.Chrome(options=chorme_options)
    brower.set_window_size(300, 200)
    apps = link_object.get_apps()
    try:
        brower.get('http://ip-api.com/json')
        brower.implicitly_wait(30)
        body = brower.find_element_by_xpath("/html/body/pre")
        print(body.text)
        print(json.JSONDecoder().decode(body.text))

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
        try:
            print("正在为您打开链接{}".format(url))
            brower.get(url)
            brower.implicitly_wait(30)
        except:
            print("打开页面长时间无响应")
            continue
        try:
            print("执行界面的滑动")
            js = "document.querySelector('#expandContent').click();setTimeout(()=>{window.scrollTo(0,10000)},1500)"
            brower.execute_script(js)
            sleep(random.randint(2, 5))
            js = "document.querySelector('.spread').click();setTimeout(()=>{window.scrollTo(0,10000)},1500)"
            brower.execute_script(js)
        except:
            pass
        print("在当前页面停留5到20秒")
        sleep(random.randint(15, 30))

    print("补时停留")
    sleep(random.randint(15, 30))

    brower.close()
    print("关闭浏览器")
    brower.quit()
    if debug is True:
        break
    if time > 20:
        break
