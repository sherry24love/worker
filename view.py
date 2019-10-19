#!/usr/bin/env python
# -*- codeing:utf-8 -*-
# gavin

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import random
import json


class view:
    """
    打开浏览器
    """
    ua = None

    links = None

    browser = None

    vpn = None

    def __init__(self, ua, links, vpn):
        self.ua = ua
        self.links = links
        self.vpn = vpn

    def run(self, times=1):
        # os.system(command)
        """ 获取可以用的APP信息 """
        time = 0
        while True:
            time = time+1
            print("The {}st time run".format(time))
            self.open()
            if time >= times:
                break

    def open(self):
        chorme_options = webdriver.ChromeOptions()
        chorme_options.set_headless()
        chorme_options.add_argument('disable-infobars')
        chorme_options.add_argument("test-type")
        chorme_options.add_argument("disable-gpu")
        chorme_options.add_experimental_option(
            "excludeSwitches", ["ignore-certificate-errors", "enable-automation"])

        """ 获取一条UA """
        ua = self.ua.get_wechat_ua()
        chorme_options.add_argument("user-agent={}".format(ua))

        ip = self.vpn.getIp()
        if ip is False:
            print("本次IP获取失败")
            return None
        elif ip != "":
            proxy = 'socks5://{}'.format(ip)
            chorme_options.add_argument("--proxy-server={}".format(proxy))
        # 设置浏览器参数
        self.browser = webdriver.Chrome(options=chorme_options)
        self.browser.set_window_size(300, 200)
        try:
            self.browser.get('http://ip-api.com/json')
            self.browser.implicitly_wait(30)
            body = self.browser.find_element_by_xpath("/html/body/pre")
            print(body.text)
            print(json.JSONDecoder().decode(body.text))
        except NoSuchElementException:
            print("IP信号不好切下一组IP")
            return None
        # check ip is ok
        apps = self.links.get_apps()
        for idx in range(len(apps)):
            print(apps[idx])
            # open {idx} tab
            self.browser.execute_script("window.open('','_blank');")
            self.browser.switch_to.window(self.browser.window_handles[-1])
            url = self.links.get_links(idx)
            try:
                print("正在为您打开链接{}".format(url))
                self.browser.get(url)
                self.browser.implicitly_wait(30)
            except:
                print("打开页面长时间无响应")
                continue
            try:
                print("执行界面的滑动")
                js = "document.querySelector('#expandContent').click();setTimeout(()=>{window.scrollTo(0,10000)},1500)"
                self.browser.execute_script(js)
                time_wait = random.randint(2, 5)
                print("等待{}秒".format(time_wait))
                sleep(time_wait)
                js = "document.querySelector('.spread').click();setTimeout(()=>{window.scrollTo(0,10000)},1500)"
                self.browser.execute_script(js)
            except:
                pass
            time_wait = random.randint(20, 50)
            print("在当前页面停留5到20秒")
            sleep(time_wait)

        print("补时停留")
        sleep(random.randint(15, 30))

        self.browser.close()
        print("关闭浏览器")
        self.browser.quit()
