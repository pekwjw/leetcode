# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = ''
        n2 = ''
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        res = str(int(n1)+int(n2))
        head = p = q = ListNode(0)
        for i in range(0,len(res)):
            q = ListNode(int(res[i]))
            p.next = q
            p = q
        return head.next
