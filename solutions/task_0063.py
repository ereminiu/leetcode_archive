class Solution:
    def uniquePathsWithObstacles(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]