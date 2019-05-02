# -*- coding:utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        for i in range(len(s)+1)[::-1]:
            for j in range(len(s)+1 - i):
                if self.isPalindrome(s[j:i+j]):
                    ans = s[j:i+j]
                    return ans
        return ''


    def isPalindrome(self,s):
        if len(s) <= 1:
            return True
        for i in range(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True


a = Solution()
print a.longestPalindrome('cbbd')
