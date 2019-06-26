# -*- coding:utf-8 -*- 

class Solution(object):
    def maxProductNums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        maxnum = minnum = ans = nums[0]
        for i in range(1,len(nums)):
            t = maxnum
            maxnum = max(t*nums[i],minnum*nums[i],nums[i])
            minnum = min(t*nums[i],minnum*nums[i],nums[i])
            ans = max(ans,maxnum)
        return ans

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        maxnum = ans = nums[0]
        for _,tmp in enumerate(nums[1:]):
            maxnum = max(maxnum+tmp,tmp)
            ans = max(maxnum,ans)
        return ans

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        elements = [0] * n
        for i,tmp in enumerate(words):
            for j in tmp:
                elements[i] = elements[i] | (1 << ord(j) - ord('a'))
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if elements[i] & elements[j] == 0:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans

a = Solution()
print a.maxProductNums([2,3,-2,4])
print a.maxSubArray([-2,1,2,3,-7,8])
print a.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
