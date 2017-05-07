#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fibonacci(object):
    def __init__(self,amount):
        self.sequence=[0,1]

    def s_add(self):
        self.sequence.append(self.sequence[-1]+self.sequence[-2])

a=int(input('长度：'))
print(a)
f=Fibonacci(a)
for x in range(a-2):
    f.s_add()
print(f.sequence)
