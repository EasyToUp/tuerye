#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :increaseFans.py
@Description  :
@Time         :2022/09/11 03:11:04
@Author       :szflvxj
@Version      :1.0
'''


tip = '你忘记记录今天的涨粉量了'
def check_growth(growth):
  if growth:
    print(growth)
  else:
    print(tip)

check_growth(input('今日涨粉量'))