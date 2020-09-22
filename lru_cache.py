# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.Next = None

class DoubleList():
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return not self.tail

    def removeLast(self):
        self.remove(self.tail)

    def remove(self, node):
        if self.head == self.tail:
            self.head = None
            self.head = None
            return

        if node == self.head:
            node.Next.prev = None
            self.head = node.Next
            return

        if node == self.tail:
            node.prev.Next = None
            self.tail = node.prev
            return

        node.prev.Next = node.Next
        node.Next.prev = node.prev

    def addFirst(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            node.Next = None
            node.prev = None
            return
        else:
            node.Next = self.head
            self.head.prev = node
            self.head = node
            node.prev = None
            return


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.P = dict()
        self.cache = DoubleList()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if (key in self.P) and self.P[key]:
            self.cache.remove(self.P[key])
            self.cache.addFirst(self.P[key])
            return self.P[key].v
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.P:
            self.cache.remove(self.P[key])
            self.cache.addFirst(self.P[key])
            self.P[key].v = value
        else :
            node = Node(key, value)
            self.P[key] = node
            self.cache.addFirst(node)
            self.size += 1
            if self.size > self.cap:
                self.size -= 1
                del self.P[self.cache.tail.k]
                self.cache.removeLast()
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
