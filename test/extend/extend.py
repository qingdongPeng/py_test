#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##继承
##定义父类 Person, 定义子类Student继承Person类

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

##继承父类, 则在括号中写父类名称
class Student(Person):
    def __init__(self, name, gender, score):
        ##一定要用super(Student, slef).__init__(name, gender)去初始化父类, 否则Student将没有name和gender
        ##调用super(Student, self)将返回当前类继承的父类, 即Person
        ##然后调用__init__方法(self参数已在super中传入, 在__init__()中将隐式传递)
        super(Student, self).__init__(name, gender)
        self.score = score

s = Student('pqd', 'Mail', '90')
print(s.name + " -- " + s.gender + " -- " + s.score)

