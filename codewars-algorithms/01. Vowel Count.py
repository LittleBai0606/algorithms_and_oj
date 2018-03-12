#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: 01. Vowel Count.py
@time: 2018/3/12 下午2:00
"""


def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowel_set = set("aeiou")
    for i in inputStr:
        if i in vowel_set:
            num_vowels = num_vowels + 1
    return num_vowels

if __name__ == '__main__':
    print(getCount("abracadabra"))