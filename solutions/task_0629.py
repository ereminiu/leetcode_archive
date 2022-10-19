class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for x in range(1228)] for y in range(1228)]
        Mod = int(1e9 + 7)
        for i in range(1, n+1):
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                prev = dp[i-1][j]
                if j-i >= 0:
                    prev -= dp[i-1][j-i]
                dp[i][j] = (dp[i][j-1] + prev) % Mod
        res = dp[n][k]
        if k > 0:
            res -= dp[n][k-1]
        return res % Mod