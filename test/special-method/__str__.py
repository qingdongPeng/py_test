#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##__str__()方法, 将一个实例转换成str, 实现特殊方法__str__()

class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '(Person: name =  %s)' % (self.name)

p = Person('pqd')
print(p)
