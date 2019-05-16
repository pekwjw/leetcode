# -*- coding:utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 1 or numRows == 1:
            return s
        ans = ['']*numRows
        n = numRows*2 - 2
        for i,m in enumerate(s):
            if i%n == 0:
                ans[0] = ans[0]+m
            for j in range(1,numRows):
                if i%n == j or i%n == n-j:
                    ans[j] = ans[j]+m
        ans = ''.join(ans)
        return ans

a = Solution()
print a.convert('ABCDEFGHIGKLMN',4) 
