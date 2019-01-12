class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList():
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """将值添加到尾部"""
        node = DoubleLinkedListNode(obj, None, None)
        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            node.prev = self.end
            self.end.next = node
            self.end = node

    def pop(self):
        """将值从尾部删除"""
        if self.begin == self.end and self.end:
            value = self.begin.value
            self.begin = self.end = None
            return value
        elif self.begin == self.end == None:
            return None
        else:
            value = self.end.value
            node = self.end.prev
            node.next = None
            self.end = node
            return value

    def shift(self, obj):
        """将值从头部添加"""
        node = DoubleLinkedListNode(obj, None, None)
        if self.begin == None:
            self.push(obj)

        else:
            self.begin.prev = node
            node.next = self.begin
            self.begin = node
            return ''

    def unshift(self):
        """将值从头部弹出并返回"""
        if self.begin == None:
            return None
        node = self.begin
        self.begin = None
        self.begin = node.next
        return node.value

    def count(self):
        node = self.begin
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def _invariant(self):
        if self.begin == None:
            assert self.end == None, "End set while begin is not."

        if self.begin:
            assert self.begin.prev == None, "begin.prev not None"
            assert self.end.next == None, "end.next not None"

    def get(self, index):
        """按照序列得到引用"""
        node = self.begin
        count = 0
        while node:
            tmp = node
            node = node.next
            if count == index:
                return tmp.value
            count += 1

    def remove(self, obj):
        """寻找匹配的元素并从中移除"""

    def dump(self, mark):
        """转储链表内容的调试函数。"""
        

    def detach_node(self, node):
        """你有时需要这个操作，但是多数都在 remove() 里面。它应该接受一个节点，将其从链表分离，无论节点是否在头部、尾部还是在中间。"""

    def first(self):
        """返回第一个元素的*引用*，不要移除。"""

    def last(self):
        """返回最后一个元素的*引用*，不要移除。"""
