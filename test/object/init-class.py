#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##__init__()方法, 当创建实例时, 此方法会自动调用, 即相当于java的构造方法

## __init__方法第一个参数必须是self(也可以为别的名字, 但建议使用习惯用法)

class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth

## 创建实例
pqd = Person("pqd", "Male", "1997-0414")
wxz = Person("wxz", "Female", "1995-0929")

print(pqd.name + "  " + pqd.gender + "  " + pqd.birth)
print(wxz.name + "  " + wxz.gender + "  " + wxz.birth)