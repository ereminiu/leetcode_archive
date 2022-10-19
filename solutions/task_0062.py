class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        #print(*dp, sep='\n')
        return dp[m-1][n-1]

# m, n = map(int, input().split())
# print(Solution().uniquePaths(m, n))