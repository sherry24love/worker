#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import os
import random


class ua:
    """
    ua 获取
    """

    current_dir = None

    wechat_ua = []

    def __init__(self):
        self.current_dir = os.path.dirname(__file__)
        print(self.current_dir)
        wechat_ua_file = os.path.join(self.current_dir, "wechat_ua.conf")
        fo = open(wechat_ua_file, 'r')
        for line in fo.readlines():  # 依次读取每行
            line = line.strip()  # 去掉每行头尾空白
            self.wechat_ua.append(line)

    def get_wechat_ua(self):
        """
        随机从数据中获取一条数据
        """
        return random.choice(self.wechat_ua)


if __name__ == "__main__":
    u = ua()
    u.get_wechat_ua()
