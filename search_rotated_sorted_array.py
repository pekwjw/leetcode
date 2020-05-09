# -*- coding:utf-8 -*-

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums :
            return -1
        right = len(nums)-1
        left = 0
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else :
                    left = mid + 1
        return -1
