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
        head = p = q = ListNode(0)
        carry = 0
        while l1 or l2:
            t = carry
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            q = ListNode(t if t<10 else t-10)
            carry = 0 if t<10 else 1
            p.next = q
            p = q
        if carry == 1:
            q = ListNode(1)
            p.next = q
        return head.next
