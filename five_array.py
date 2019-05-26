# -*- coding:utf-8 -*-

class Solution_setZeros(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        if m == 0 or n == 0:
            return
        record = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    record.append([i,j])
        for _,tmp in enumerate(record):
            r,c = tmp[0],tmp[1]
            for i in range(n):
                matrix[r][i] = 0
            for j in range(m):
                matrix[j][c] = 0


class Solution_sortColors(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for _,tmp in enumerate(nums):
            count[tmp] += 1
        head = end = 0
        for index,tmp in enumerate(count):
            end += tmp
            for i in range(head,end):
                nums[i] == index
            head = end


class Solution_sm(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0 :
            return False
        n = len(matrix[0])
        if n == 0 :
            return False
        for i in range(m):
            if target <= matrix[i][-1]:
                for j in range(n):
                    if target == matrix[i][j]:
                        return True
        return False


class Solution_fpe(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        else:
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (right+left)/2
                if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] > nums[mid]:
                    right = mid-1
                else:
                    left = mid+1


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        head = cur = nums[0]
        ans = []
        for i in range(1,len(nums)):
            if nums[i] == cur+1:
                cur += 1
            else:
                if head < nums[i-1]:
                    ans.append(str(head)+"->"+str(nums[i-1]))
                    head = nums[i]
                    cur = nums[i]
                elif head == nums[i-1]:
                    ans.append(str(head))
                    head = nums[i]
                    cur = nums[i]
        if head < nums[-1]:
            ans.append(str(head)+'->'+str(nums[-1]))
        else:
            ans.append(str(head))
        return ans

a = Solution()
print a.summaryRanges([0,1,2,4,5,7])
print a.summaryRanges([0,2,3,4,6,8,9])
