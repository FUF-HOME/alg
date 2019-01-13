#!/usr/bin/env python
# -*-coding:utf-8-*-
class Queue():

    def __init__(self):
        self.data = []

    def enQueue(self,value):
        self.data.append(value)

    def deQueue(self):
        value = self.data.pop(0)
        return value
    def clear(self):
        self.data = []

    def get_size(self):
        return len(self.data)