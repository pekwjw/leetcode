# -*- coding:utf-8 -*-

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if dividend == -pow(2,31) and divisor == -1:
            return pow(2,31)-1
        ans = 0
        d1 ,d2 = abs(dividend),abs(divisor)
        while d1 >= d2 :
            tmp = d2
            p = 1
            while d1 >= (tmp << 1):
                tmp = tmp << 1
                p = p << 1
            ans += p
            d1 -= tmp
        if (dividend<0) ^ (divisor<0) == 1:
            return 0-ans
        return ans

a = Solution()
print a.divide(-7,-3)
print a.divide(7,-3)
print a.divide(-2147483648,-1)
print a.divide(2147483647,1)
