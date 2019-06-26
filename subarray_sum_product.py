# -*- coding:utf-8 -*- 

class Solution(object):
    def maxProduct(self, nums):
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
    
a = Solution()
print a.maxProduct([2,3,-2,4])
print a.maxSubArray([-2,1,2,3,-7,8])
