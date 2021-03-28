#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, hid, district, postion, area, name, price, unitPrice, followInfo, desc, subway, pic):
        self.hid = hid
        self.district = district
        self.area = area
        self.postion = postion
        self.price = price
        self.name = name
        self.followInfo = followInfo
        self.unitPrice = unitPrice
        self.desc = desc
        self.pic = pic
        self.subway = subway

    def text(self):
        return  self.district + "," + \
                self.area + "," + \
                self.postion + "," + \
                self.hid + "," + \
                self.name + "," + \
                self.price + "," + \
                self.unitPrice + "," + \
                self.followInfo + "," + \
                self.subway + "," + \
                self.desc + "," + \
                self.pic
