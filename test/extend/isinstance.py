#!/usr/bin/env python 
# -*- coding:utf-8 -*-

## isinstance()方法可以用来判断一个变量的类型, 如str, list, dict， 语法isinstance(obj, Class)
## 也可以用在自定义的类

##issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)

s = 'pqd'
print(isinstance(s, str))

l = s.split()
print(isinstance(l, list))

class Person(object):
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, score):
        super(Student, self).__init__(name)
        self.score = score

p = Person('pqd')
print(isinstance(p, Person))

s = Student('pqd', '90')
## 在一条继承链上, 一个对象可以看作它本身的类型, 也可以看作是它父类的类型
print(isinstance(s, Student))
print(isinstance(s, Person))

##一条继承链上, 一个父类对象不能是子类类型, 因为子类比父类多了一些属性和方法
print(isinstance(p, Student))


## issubclass判断一个类是另一个类的子类或者子孙类
print(issubclass(Student, Person))
print(issubclass(Person, Student))
print(issubclass(Student, list))