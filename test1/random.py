#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def generate_code(len):
    ## 生成指定长度的验证码
    all_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for _ in range(len):
        index = random.randint(0, len(all_chars) -1)
        print(all_chars[index])

generate_code()