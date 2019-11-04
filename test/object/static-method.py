#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##定义类方法, 即无需new对象来调用, 相当于java中静态方法
##用@classmethod注解来实现

class Person(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

    #类方法
    @classmethod
    def how_many(cls):
        return cls.count

print(Person.how_many())
p = Person("pqd")
print(Person.how_many())