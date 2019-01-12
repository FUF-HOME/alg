class BSTreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def find_minimum(self):
        node = self
        while node.left:
            node = node.left
        return node

    def replace_child(self, child):
        """Given a child, it will find the child, move it's value to here, then remove it.
        Copied from wikipedia to solve it quicker.
        """
        if self.parent:
            if self == self.parent.left:
                self.parent.left = child
            else:
                self.parent.right = child

        if child:
            child.parent = self.parent

    def __repr__(self):
        return f"{self.key}={self.value}:<--- ({self.left}) ---> ({self.right})"


class Bstree:
    def __init__(self):
        self.root = None

    def search(self, node, parent, value):
        if node is None:
            return False, node, parent
        elif node.value == value:
            return True, node, parent
        elif node.value > value:
            return self.search(node.left, node, value)
        else:
            return self.search(node.right, node, value)

    def insert(self, key, value):
        if self.root == None:
            self.root == BSTreeNode(key, value)
        else:
            node = self.root
            while node:
                if node.key == key:
                    node.value = value
                    break
                elif node.left == None and node.right == None:
                    if key < node.key:
                        node.left = BSTreeNode(key, value, parent=node)
                    else:
                        node.right = BSTreeNode(key, value, parent=node)
                    break
                elif key < node.key:
                    if node.left:
                        node = node.left
                    else:
                        node = BSTreeNode(key, value, parent=node)
                elif key >= node.key:
                    if node.right:
                        node = node.right
                    else:
                        node = BSTreeNode(key, value, parent=node)
                else:
                    assert False, "Should not happen"

    def in_ordeded(self, node):
        self.in_ordeded(node.left)
        print(node.value)
        self.in_ordeded(node.right)

    def pre_oderde(self, node):
        print(node.value)
        self.pre_oderde(node.left)
        self.pre_oderde(node.right)

    def clear(self, node):
        if node and node is BSTreeNode:
            self.clear(node.left)
            self.clear(node.right)
            node = None

    def isEmpty(self):
        return self.root == None

    def height(self, node):
        node = self.root
        if node:
            return 0
        else:
            l = self.height(node.left)
            r = self.height(node.right)
            return 1 < r if r + 1 else l + 1
