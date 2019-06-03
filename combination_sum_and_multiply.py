# -*- coding:utf-8 -*-

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pass

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pass

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = len(num1),len(num2)
        ans = [0]*(n1+n2)
        first = num1[::-1]
        second = num2[::-1]
        for i in range(n1):
            for j in range(n2):
                ans[i+j] += int(first[i])*int(second[j])
        carry = 0
        res = ""
        for i,tmp in enumerate(ans):
            ans[i] = (tmp+carry)%10
            carry = (tmp+carry)/10
        carry = 1
        for i in ans[::-1]:
            if carry and i == 0:
                pass
            else:
                carry = 0
                res += str(i)
        return res
a = Solution()
print a.multiply("999","999") 
