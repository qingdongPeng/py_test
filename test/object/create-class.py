#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##创建类
## python 是动态语言, 对于每一个实例, 可以直接给他们的属性赋值
class Student(object):
    pass

xiaoming = Student()
xiaoming.name = "xiaoming"

xiaohong = Student()
xiaohong.name = "xiaohong"

xiaoqiang = Student()
xiaoqiang.name = "xiaoqiang"

list = [xiaoming, xiaohong, xiaoqiang]

for a in list:
    print(a.name)

print(xiaoming == xiaohong)
