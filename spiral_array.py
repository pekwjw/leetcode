# -*- coding:utf-8 -*-

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        left = 0
        right = len(matrix[0])-1
        up = 0
        down = len(matrix)-1
        ans = []
        while left <= right and up <= down:
            for i in range(left,right+1):
                ans.append(matrix[up][i])
            up = up+1
            if up > down:
                break
            for i in range(up,down+1):
                ans.append(matrix[i][right])
            right = right-1
            if right < left:
                break
            for i in range(right,left-1,-1):
                ans.append(matrix[down][i])
            down = down-1
            if up > down:
                break
            for i in range(down,up-1,-1):
                ans.append(matrix[i][left])
            left += 1
        return ans

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        ans = [[0 for i in range(n)] for i in range(n)]
        left = 0
        right = n-1
        up = 0
        down = n-1
        cur = 0
        while cur<= n*n and left<=right and up<=down:
            for i in range(left,right+1):
                cur += 1
                ans[up][i] = cur
            up = up+1
            if up > down:
                break
            for i in range(up,down+1):
                cur += 1
                ans[i][right] = cur
            right = right-1
            if left > right :
                break
            for i in range(right,left-1,-1):
                cur+=1
                ans[down][i] = cur
            down = down-1
            if up > down:
                break
            for i in range(down,up-1,-1):
                cur+=1
                ans[i][left] = cur
            left = left+1
        return ans

    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        pass

a = Solution()
a.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
print a.generateMatrix(3)
