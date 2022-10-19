class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = int(1e9+7)
        MX = 1001
        dp = [[0 for x in range(MX)] for y in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for sum in range(MX):
                for x in range(1, k+1):
                    dp[i][sum] += dp[i-1][sum-x]
                    if dp[i][sum] >= mod:
                        dp[i][sum] -= mod
        return dp[n][target]

# n, k, target = map(int, input().split())
# print(Solution().numRollsToTarget(n, k, target))