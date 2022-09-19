#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :birthyear.py
@Description  :
@Time         :2022/09/09 21:49:35
@Author       :szflvxj
@Version      :1.0
'''

birth_year = int(input("你哪年被弄出来的？"))
if birth_year > 2022:
    print("你做梦呢？你算个卵东西")
elif birth_year == 2022:
    print("哦，你爸妈正在造你呢！")
elif 1940 < birth_year < 2022:
    def calc_age(birth_year):
        age = 2022 - birth_year
        return age
print("你现在" + str(calc_age(birth_year)) + "岁")
if birth_year <= 1940:
    def calc_age_old(birth_year):
        age_old = 2022 - birth_year
        return age_old
print("?" + str(calc_age_old(birth_year)) + "岁?你还挺能活")


def calc_age(birth_year):
    age = 2022 - birth_year
    if age < 0:
        print("你做梦呢？你算个卵东西")
    else:
        return age


# result = calc_age()
# print(result)
print(calc_age(int(input("你哪年被弄出来的？"))))

# print ("你大爷我的年龄是" + str(calc_age(2003)))
# print(calc_age(int(input("你哪年被弄出来的？")))
