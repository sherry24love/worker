#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


class links:

    """ 开发模式 """
    debug = False

    def __init__(self, debug=False):
        self.debug = debug

    def get_apps(self):
        """ 获取APP信息 """
        return [
            {
                "name": "百家姓",
                "code": "bjx"
            },
            {
                "name": "金元宝",
                "code": "jyb"
            }
        ]

    def get_links(self, index):
        """ 获取可用链接 """
        url = [
            "http://god.kzijhws.cn/ln/zlwegnonmmjwsiGfw.do?from=timeline",
            "http://god.mnjkj.cn/wL/ujyiylncxjyqwbsiGhy.shtml?from=timeline",
            "http://wsd.esezfv.cn/TepXK/bjdhqunppegsiGjlxl.do?from=timeline",
            "http://wsd.grpmqw.cn/GdwT/pepjdlyhapgsiGjn.htm?from=timeline",
            "http://wsd.gdwdvf.cn/loB/pfbvhvjnvzunsiGuh.htm?from=timeline",
            "http://god.gnffrs.cn/GPGLdV/xoopnpupneesiGiq.shtml?from=timeline",
            "http://nesw.rsjwnuuv.cn/wW/agugmmdxdlsiGikex.htm?from=timeline",
            "http://nesw.rsjwnuuv.cn/mmFZOf/fxlyllnplxysiGcz.do?from=timeline",
            "http://god.xgaeh.cn/HjPa/ugcyamlyydxsiGvgxf.htm?from=timeline"
        ]
        if self.debug is True:
            url = [
                "http://www.baidu.com"
            ]
        return random.choice(url)
