#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from utils.vpn import vpn
from utils.ua import ua as user_agent
from utils.links import links
import configparser
import json
import os
from view import view


class gun:

    _main_box_ = None

    def __init__(self):
        self._main_box_ = Tk(className="Gavin")
        self._main_box_.geometry("500x300")
        self.setip()
        self._main_box_.mainloop()

    def setip(self):

        pass

    pass


debug = True
#gui = gun()
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
view = view(user_agent_object, link_object, v)
view.run(1)
