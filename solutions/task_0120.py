class Solution:
    def minimumTotal(self, triangle) -> int:
        a = triangle
        n = len(triangle)
        dp = [[0] for x in range(n)]
        dp[0][0] = a[0][0]
        for i in range(1, n):
            dp[i] = (i+1)*[int(1e9+228)]
            for j in range(i+1):
                if j < i:
                    dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                dp[i][j] += a[i][j]
            #print(dp[i])
        return min(dp[n-1])