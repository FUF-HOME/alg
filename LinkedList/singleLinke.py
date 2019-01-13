class SingleNode():
    """链表节点"""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self,):
        self.__head = None

    def push(self, obj):
        """将新的值附加到链表尾部。"""
        node = SingleNode(obj)
        if self.__head == None:
            self.__head = node
        else:
            pre = self.__head
            while pre.next:
                pre = pre.next
            pre.next = node

    def pop(self):
        """移除最后一个元素并返回它。"""
        if self.__head == 0:
            return None
        elif self.__head.next == None:
            node = self.__head
            middle = node
            self.__head = None
            return middle.value
        node = self.__head
        while node.next:
            pre = node
            node = node.next
        middle = node
        pre.next = None
        return middle.value

    def shift(self, obj):
        """将新的值附加到链表头部。"""
        node = SingleNode(obj)
        node.next = self.__head
        self.__head = node

    def unshift(self):
        """移除第一个元素并返回它。"""
        if self.__head == None:
            return None
        node = self.__head
        self.__head = self.__head.next
        return node.value

    def remove(self, obj):
        """寻找匹配的元素并从中移除。"""
        node = self.__head
        pre = None
        count = 0
        while node:
            currnet = node
            node = node.next
            if currnet.value == obj:
                if pre == None and node:
                    self.__head = node
                    return count
                else:
                    currnet.next = None
                    pre.next = node
                    return count
            count += 1
            pre = node

    def first(self):
        """返回第一个元素的*引用*，不要移除。"""

    def last(self):
        """返回最后一个元素的*引用*，不要移除。"""

    def count(self):
        """计算链表中的元素数量。"""
        node = self.__head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """获取下标处的值。"""
        node = self.__head
        target = 0 
        while node:
            if target == index:
                return node.value
            node =node.next
            target +=1
        return None

    def dump(self, mark):
        """转储链表内容的调试函数。"""
        mark = mark
        node = self.__head
        # new_head = None
        if mark == 'before perinone':
            if node == None or node.next == None:
                return node
            while node:
                tmp = node.next
                node.next = new_head
                new_head = node
                node = tmp
            self.__head = new_head
