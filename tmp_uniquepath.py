# -*- coding:utf-8 -*-

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[ 0 for i in range(n)] for j in range(m)]
        for j in range(n):
            if obstacleGrid[m-1][j]:
                break
            else:
                dp[m-1][j] = 1
        for i in range(m):
            if obstacleGrid[i][n-1]:
                break
            else:
                dp[i][n-1] = 1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] == 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
a = Solution()
print a.uniqurPathsWithObstacles()    
