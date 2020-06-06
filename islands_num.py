class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nrow = len(grid)
        if nrow == 0:
            return 0

        ncolumn = len(grid[0])
        nislands = 0

        for i in range(nrow):
            for j in range(ncolumn):
                if grid[i][j] == "1":
                    nislands += 1
                    self.dfs(grid, i, j, nrow, ncolumn)
        return nislands

    def dfs(self, grid, i, j, nrow, ncolumn):
        grid[i][j] = '0'
        for x, y in [(i-1, j),(i+1, j), (i,j-1),(i,j+1)]:
            if  0<=x < nrow and 0<= y < ncolumn and grid[x][y] == '1':
                self.dfs(grid, x, y, nrow, ncolumn)

    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        ncislands = 0

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 0:
                    self.val = 1
                    self.dfsc(grid, i, j, nr, nc)
                    ncislands += self.val

        return ncislands

    def dfsc(self, grid, x, y, nr, nc):
        if x < 0 or x >= nr or y < 0 or y >= nc:
            self.val = 0
            return

        if grid[x][y] != 0:
            return

        grid[x][y] = 1
        self.dfsc(grid, x+1, y, nr, nc)
        self.dfsc(grid, x-1, y, nr, nc)
        self.dfsc(grid, x, y+1, nr, nc)
        self.dfsc(grid, x, y-1, nr, nc)

print Solution().closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])

print Solution().numIslands([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']])
