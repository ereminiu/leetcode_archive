class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1); m = len(text2)
        dp = [[0 for x in range(m)] for y in range(n)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (dp[i-1][j-1] if i > 0 and j > 0 else 0)
                else:
                    if i > 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])
        # print(*dp, sep='\n')
        return dp[n-1][m-1]