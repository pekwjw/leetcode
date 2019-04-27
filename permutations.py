# -*- coding:utf-8 -*-

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                tmp = [num] + y
                if tmp in ans:
                    pass
                else:
                    ans.append([num] +y)
        return ans

a = Solution()
print a.permute([1,2,1])
