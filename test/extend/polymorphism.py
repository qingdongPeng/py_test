#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##多态

class Person(object):
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("my name is " + self.name)

class Student(Person):
    def __init__(self, name, score):
        super(Student, self).__init__(name)
        self.score = score

    def printName(self):
        print("my name is " + self.name)

p = Person('pqd')
p.printName()

s = Student('wxz', '90')
##如果子类没有printName方法, 则会向上查找, 直到在某个父类中找到为止
s.printName()