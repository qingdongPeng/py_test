#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##方法也可以作为参数传入
def add(a, b, f):
    return f(a) + f(b)


print(add(1, -2, abs))
