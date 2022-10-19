class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s, t = word1, word2
        n, m = len(s), len(t)
        dp = [[0 for x in range(m+1)] for y in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                    continue
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (1 if s[i-1] != t[j-1] else 0))
        return dp[n][m]