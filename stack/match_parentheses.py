#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
利用栈实现括号匹配

"""



from .stack import Stack

class Valid():
    def __init__(self):
        self.stack = Stack()

    def isValid(self,parentheses):
        if len(parentheses) == 0:
            return False
        for p in parentheses:
            if p == '(' or p == '{' or p == '[':
                self.stack.push(p)

            else:

                if self.stack.isEmpty():
                    return False
                topChar = self.stack.pop()
                if p == ')' and topChar != '(':
                    return False
                elif p == '}' and topChar != '{':
                    return False
                elif p ==']' and topChar !='[':
                    return False
        return self.stack.isEmpty()