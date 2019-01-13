#!/usr/bin/env python
# -*-coding:utf-8-*-

class Stack():
    def __init__(self):
        self.element = []

    def isEmpty(self):
        if len(self.element) == 0:
            return True
        else:
            return False

    def get_size(self):
        return len(self.element)

    def pop(self):
        value=self.element.pop(-1)
        return value

    def push(self,value):
        self.element.append(value)

    def peek(self):
        value=self.element[-1]
        return value
