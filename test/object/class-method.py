#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##私有属性外部无法访问, 从内部却可以访问, 所以在实例内部可以提供方法给外部访问该属性

class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    ##实例方法
    def get_name(self):
        return self.__name

    def get_grade(self):
        if self.__score >= 80:
            return "A"
        if self.__score >= 60:
            return "B"
        else:
            return "C"


pqd = Person("pqd", 6)
print(pqd.get_name())

p1 = Person("p", 90)
print(p1.get_grade())

p2 = Person("p", 70)
print(p2.get_grade())

p3 = Person("p", 50)
print(p3.get_grade())