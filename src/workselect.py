#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :workselect.py
@Description  :return很折磨人
@Time         :2022/09/11 03:12:20
@Author       :szflvxj
@Version      :1.0
'''

money = 1000


def work(add):
    new = money + add
    global zq
    zq = add
    print(zq)
    return new


new1 = work(int(input("你赚多少钱")))
print(new1)
print(zq)
zq1 = str(zq)
print(zq1)
print('赚了' + zq1 + '还剩' + str(new1))
