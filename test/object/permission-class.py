#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##在一个实例中, 有些属性不希望被外部访问, 用双下划线开头, 即外部无法访问该属性
##以__xxx__定义的属性被称为特殊属性, 可以被外部访问
class Person(object):
    def __init__(self, name):
        self.name = name
        self.__job = 'Student'

pqd = Person("pqd")
print(pqd.name)

## 会报错, 因为job外界无法访问
## print(pqd.__job)

