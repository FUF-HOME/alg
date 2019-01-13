#!/usr/bin/env python
# -*-coding:utf-8-*-

class LinkedListNode():
    """链表节点"""

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return '{}'.format(self.data)


class LinkedListQueue():
    """使用链表实现队列"""
    def __init__(self):
        self.begin = None
        self.next = None
        self.tail = None
        self.size = 0

    def dequeue(self):
        '''从队列中弹出一个元素'''
        if self.isEmpty():
            print('队列里面已经没有元素!')
            return False
        else:
            p_node = self.begin
            self.begin = self.begin.next
            self.size -= 1
            return p_node.data

    def enqueue(self, obj):
        '''往队列中加入一个元素'''
        node = LinkedListNode(obj)
        if self.begin == None:
            self.begin = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def get_size(self):
        '''队列元素count'''
        return self.size

    def peek(self):
        '''得到队列的头部的元素，但不删除'''
        return self.begin.data

    def isEmpty(self):
        if self.get_size() == 0:
            return True
        else:
            return False

    def _print(self):
        '''打印队列'''
        list_node = []
        node = self.begin
        while node:
            list_node.append(node.data)
            node = node.next

        return list_node

    def dump(self):
        '''逆转队列'''
        node = self.begin
        new_node = None
        while node:
            tmp = node.next
            node.next = new_node
            new_node = node
            node =tmp
        midell = self.begin
        self.begin = self.tail
        self.tail = midell
        self.tail.next = None
