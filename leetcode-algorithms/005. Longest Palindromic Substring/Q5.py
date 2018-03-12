#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: Q5.py
@time: 2018/3/12 下午2:19
"""

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return
        n = len(s)
        if n == 1:
            return s
        l = 0
        r = 0
        m = 0
        c = 0
        b = True
        for i in range(0, n):
            # odd
            for j in range(0, min(n-i, i+1)):
                if(s[i-j] != s[i+j]):
                    b = False
                    break
                else:
                    c = 2*j+1

            if(c > m):
                l = i-j+1-b
                r = i+j+b
                m = c
            b=True

            # even
            for j in range(0, min(n-i-1, i+1)):
                if(s[i-j] != s[i+j+1]):
                    b = False
                    break
                else:
                    c = 2*j+2

            if(c > m):
                l = i-j+1-b
                r = i+j+1+b
                m = c
            b = True
        return s[l:r]






