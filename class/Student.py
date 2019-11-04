#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Student(object):

    ## init 为初始化方法
    def __init__(self, name, age):
        ## self.__name = name   如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
        self.name = name
        self.age = age

    def study(self, coruse):
        print("%s 正在学习 %s" % (self.name, coruse))

    def movie(self):
        if self.age < 18:
            print("%s 在看熊出没" % self.name)
        else:
            print("%s 在看大片" % self.name)

def main():
    stu = Student("pqd", 22)
    stu.study("math")
    stu.movie()

if __name__ == '__main__':
    main()