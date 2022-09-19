#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :area.py
@Description  :
@Time         :2022/09/09 21:48:51
@Author       :szflvxj
@Version      :1.0
'''


def area(r):
    area = 3.14 * r * r
    print("该圆的面积是" + str(area))


area(int(input("你想画的圆半径是多少？")))
