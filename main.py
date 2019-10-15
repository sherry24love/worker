#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from utils.ua import ua


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


if __name__ == "__main__":
    #gui = gun()
    u = ua()
    ua = u.get_wechat_ua()
    print(ua)
