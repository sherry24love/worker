#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import os


class links:

    """ 开发模式 """
    debug = False
    links = {}

    def __init__(self, debug=False):
        self.debug = debug

    def get_apps(self):
        """ 获取APP信息 """
        apps = [
            {
                "name": "百家姓",
                "code": "bjx"
            },
            {
                "name":"土拨鼠",
                "code":"tbs"
            }
        ]
        self.current_dir = os.getcwd()
        for app in apps:
            code = app["code"]
            self.links[code] = []
            link_file = os.path.join(
                self.current_dir, "data", "{}.txt".format(code))
            fo = open(link_file, 'r')
            for line in fo.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                self.links[code].append(line)
            fo.close()
        return apps

    def get_links(self, index):
        """ 获取可用链接 """
        apps = self.get_apps()
        app = apps[index]
        code = app["code"]
        url = self.links[code]
        if self.debug is True:
            url = [
                "http://www.baidu.com"
            ]
        return random.choice(url)
