#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author gavin

import requests


class vpn:

    debug = False
    """
    获取IP的址
    """
    url = None

    def __init__(self, url, debug=False):
        """ 初始化vpn """
        self.debug = debug
        self.url = url

    def getIp(self):
        if self.debug is True:
            return ""

        """ 获取可用的IP """
        url = "http://http.tiqu.alicdns.com/getip3?num=1&type=1&pro=440000&city=0&yys=100017&port=2&pack=67747&ts=0&ys=0&cs=0&lb=3&sb=0&pb=45&mr=2&regions="
        url = self.url
        result = requests.get(url)
        if result.status_code == 200:
            result.encoding = 'utf-8'
            ip = result.text
            print(ip)
            """ 检查ip 是不是正常取到了 """
            if ip.startswith("{") is True:
                return False
            return ip
        else:
            print("获取IP失败")


if __name__ == "__main__":
    v = vpn()
    v.getIp()
