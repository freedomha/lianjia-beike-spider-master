#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ChengJiao(object):
    def __init__(self, district, area, name, price, dealDate):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.dealDate = dealDate
        

    def text(self):
        return  self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.dealDate
                
