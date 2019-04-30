# -*- coding:utf-8 -*-

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cursor = 0
        for _,v in enumerate(nums):
            if v != val :
                nums[cursor] = v
                cursor += 1
        return cursor

a = Solution()
print a.removeElement([3,2,3,2],3)
print a.removeElement([0,1,2,2,3,0,4,2],2)
