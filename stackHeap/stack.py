class Heap():
    """堆是一般可以认为是一个特殊的完全二叉树
    现在实现一个最大堆

    """
    def __init__(self,A):
        self.S = A[:]
        self.size = self.heap_size = len(A)
        self._BUILD_MAX_HEAP()
    PARENT = lambda self, i: i/2 #获得i的父结点下标
    LEFT = lambda self, i: 2*i # 获得i的左子树的根结点下标
    RIGHT = lambda self, i: 2*i+1 # 获得i的右子树的根结点下标

    def isEmpty(self):
        if self.element[0] == 0 :
            return True
        else:
            return False

    def MAX_HEAPIFY(self,value):
        """插入一个值"""
        if self.isEmpty():
            self.element.append(value)




    def height(self):
        height = len(self.element) -1
        return height

    def _print(self):
        return self.element