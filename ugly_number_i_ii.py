# -*- coding:utf-8 -*-

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ans = [1]
        factor = [2,3,5]
        i2 = i3 = i5 = 0
        while len(ans) < n:
            m2 = ans[i2]*2
            m3 = ans[i3]*3
            m5 = ans[i5]*5
            mn = min(m2,m3,m5)
            ans.append(mn)
            if mn == m2:
                i2 += 1
            if mn == m3:
                i3 += 1
            if mn == m5:
                i5 += 1
        return ans[-1]
 

a = Solution()
a.nthUglyNumber(1)
for i in range(20):
    print a.nthUglyNumber(i) 
