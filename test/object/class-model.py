#!/usr/bin/env python 
# -*- coding:utf-8 -*-

## 实例属性每个实例各自拥有, 互相独立, 而类属性有且只有一份

class Person(object):
    address = "Earth"
    def __init__(self, name):
        self.name = name

## 因为类属性是绑定在类上的, 所以访问类属性无需创建实例就可访问
print(Person.address)

## 对一个实例调用类的属性也是可以访问的, 所有实例都可以访问到它所属的类的属性
pqd = Person("pqd")
print(pqd.address)

## 类属性也可以动态添加和修改
Person.address = "China"
print(Person.address)