#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
利用链表实现栈

"""

class LinkedNode(object):
    '''链表节点'''
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"self.data"


class LinkedListStacks(object):

    def __init__(self):
        self.begin = None
        self.size = 0

    def push(self, obj):
        '''入栈'''
        node = LinkedNode(obj)
        if self.begin == None:
            self.begin = node

        else:
            node.next = self.begin
            self.begin = node
        self.size += 1

    def pop(self):
        '''出栈'''
        head_node = self.begin
        if head_node:
            self.size -= 1
            self.begin = head_node.next
        else:
            return False

        return head_node.data

    def peek(self):
        '''显示栈头元素'''
        return self.begin.data

    def get_size(self):
        ''''''
        return self.size
