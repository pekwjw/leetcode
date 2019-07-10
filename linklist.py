# -*- coding:utf-8 -*-

# definition
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def createList(vals):
    head = ListNode(-1)
    p = head
    for i in vals:
        q = ListNode(i)
        p.next, p = q, q
    return head.next

def printList(head):
    while head:
        print head.val
        head = head.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pass

if __name__ == "__main__": 
    pass
