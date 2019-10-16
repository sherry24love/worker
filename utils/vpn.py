#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author gavin

import requests


class vpn:

    debug = False

    def __init__(self, debug=False):
        """ 初始化vpn """
        self.debug = debug

    def getIp(self):
        if self.debug is True:
            return ""

        """ 获取可用的IP """
        url = "http://http.tiqu.alicdns.com/getip3?num=1&type=1&pro=440000&city=0&yys=100017&port=2&pack=67747&ts=0&ys=0&cs=0&lb=3&sb=0&pb=45&mr=2&regions="
        url = "http://http.tiqu.alicdns.com/getip3?num=1&type=1&pro=440000&city=0&yys=100017&port=2&pack=67747&ts=0&ys=0&cs=0&lb=3&sb=0&pb=45&mr=2&regions="
        result = requests.get(url)
        if result.status_code == 200:
            result.encoding = 'utf-8'
            ip = result.text
            print(ip)
            return ip
        else:
            print("获取IP失败")


if __name__ == "__main__":
    v = vpn()
    v.getIp()
