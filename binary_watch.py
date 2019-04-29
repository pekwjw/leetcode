# -*- coding:utf-8 -*-

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for n in range(1024):
            if bin(n).count('1') == num:
                h,m = n >> 6, n & 0x3F
                if h < 12 and m < 60:
                    ans.append('%d:%02d' % (h,m))
        return ans

a = Solution()
print a.readBinaryWatch(1)
