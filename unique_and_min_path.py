class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[ 0 for i in range(n)] for j in range(m)]
        for j in range(n-1,-1,-1):
            if obstacleGrid[m-1][j]:
                break
            else:
                dp[m-1][j] = 1
        for i in range(m-1,-1,-1):
            if obstacleGrid[i][n-1]:
                break
            else:
                dp[i][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] == 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        dp = [[ 0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = grid[i][0]+dp[i-1][0]
        for j in range(1,n):
            dp[0][j] = grid[0][j]+dp[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix),len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                else:
                    dp[i][j] = 0
        ans = max([max(i) for i in dp])
        return ans**2

a = Solution()
print a.uniquePaths(7,3)
print a.uniquePathsWithObstacles([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0]])
print a.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
