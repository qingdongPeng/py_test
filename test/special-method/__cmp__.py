#!/usr/bin/env python 
# -*- coding:utf-8 -*-

##__cmp__()方法用来排序

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return 'Student : name = %s, score = %s' % self.name, self.score

    ##重写排序方法__cmp__  先按成绩排序, 成绩一样按姓名排序
    def __cmp__(self, other):
        if self.score == other.score:
            return __cmp__(self.name, other.name)
        return __cmp__(self.score, other.score)

l = [Student('pqd', 99), Student('pdd', 88), Student('wxz', 100)]
print(sorted(l, key=lambda student:(student.score, student.name)))